FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel
WORKDIR /home  
COPY req.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

EXPOSE 8888