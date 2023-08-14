import io 
import streamlit as st
import torch
from torch.nn import functional as F
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw
import plotly.express as px
from easyocr import Reader
from transformers import (
    LayoutLMv3FeatureExtractor, 
    LayoutLMv3TokenizerFast, 
    LayoutLMv3Processor, 
    LayoutLMv3ForSequenceClassification,
)

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
MICROSOFT_MODEL_NAME = "microsoft/layoutlmv3-base"
MODEL_NAME = "humanai2025/layoutlmv3-fdc"



def create_bounding_box(bbox_data, width_scale: float, height_scale: float):
    xs = []
    ys = []
    for x, y in bbox_data:
        xs.append(x)
        ys.append(y)

    left = int(min(xs) * width_scale)
    top = int(min(ys) * height_scale)
    right = int(max(xs) * width_scale)
    bottom = int(max(ys) * height_scale)

    return [left, top, right, bottom]


def predict_document_image(
    image: Image,
    reader: Reader,
    model: LayoutLMv3ForSequenceClassification,
    processor: LayoutLMv3Processor):

    
    ocr_result = reader.readtext(image)
    width, height = image.size
    width_scale = 1000 / width
    height_scale = 1000 / height

    new_image = Image.new("RGB", image.size, (255, 255, 255))
    image_draw = ImageDraw.Draw(new_image)

    for i, (bbox, word, confidence) in enumerate(ocr_result):
        box = create_bounding_box(bbox, width_scale, height_scale)
        left, top, right, bottom = box
        image_draw.text((left, top), text=word, fill="black")


    words = []
    boxes = []

    for bbox, word, _ in ocr_result:
        words.append(word)
        boxes.append(create_bounding_box(bbox, width_scale, height_scale))
        encoding = processor(
            image,
            words,
            boxes=boxes,
            max_length=512,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

    with torch.inference_mode():
        output = model(
            input_ids=encoding["input_ids"].to(DEVICE),
            attention_mask=encoding["attention_mask"].to(DEVICE),
            bbox=encoding["bbox"].to(DEVICE),
            pixel_values=encoding["pixel_values"].to(DEVICE)
        )

    predicted_class = output.logits.argmax()
    probabilities = F.softmax(output.logits, dim=1).flatten().tolist()
    return predicted_class.detach().item(), probabilities, image


# experimental singleton is used to load the model once and save it in memory for the whole session  


@st.experimental_singleton
def create_ocr_reader():
    return Reader(['en'])

@st.experimental_singleton
def create_processor():
    feature_extractor = LayoutLMv3FeatureExtractor(apply_ocr=False)
    tokenizer = LayoutLMv3TokenizerFast.from_pretrained("microsoft/layoutlmv3-base")
    return LayoutLMv3Processor(feature_extractor, tokenizer)

@st.experimental_singleton
def create_model():
    model = LayoutLMv3ForSequenceClassification.from_pretrained("humanai2025/layoutlmv3-fdc")
    return model.eval().to(DEVICE)


# These will take time for model files downloading
reader = create_ocr_reader()
processor = create_processor()
model = create_model()

uploaded_file = st.file_uploader("Upload Document Image", ["jpg", "png"])
if uploaded_file is not None:
    bytes_data = io.BytesIO(uploaded_file.getvalue())
    image = Image.open(bytes_data)
    predicted_class, probabilities, new_image = predict_document_image(image=image, reader=reader,model=model, processor=processor)
    print(predicted_class, probabilities)
    st.image(image, "The Document Uploaded")
    st.image(new_image, "The Document patches identified")

    predicted_label = model.config.id2label[predicted_class]
    st.markdown(f"Predicted document type: **{predicted_label}**")
    df_predictions = pd.DataFrame(
        {"Document": list(model.config.id2label.values()),
         "Confidence": probabilities}
    )
    fig = px.bar(df_predictions, x="Document", y="Confidence")
    st.plotly_chart(fig, use_container_width=True)



