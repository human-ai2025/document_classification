<div align="center" id="top"> 
  <img src="https://github.com/human-ai2025/document_ocr_classification/blob/main/img/bdad83da09760e40dc4c353c627df6678d58209c6479c169270daf2d.jpg" alt="Document_classification" />

  &#xa0;

  <!-- <a href="https://document_classification.netlify.app">Demo</a> -->
</div>

<h1 align="center">Document Ocr Classification</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/human-ai2025/document_ocr_classification?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/human-ai2025/document_ocr_classification?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/human-ai2025/document_ocr_classification?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/human-ai2025/document_ocr_classification?color=56BEB8">


</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Document_classification 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/human-ai2025" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This project is about document data extraction and document classification. 

## :sparkles: Features ##

:heavy_check_mark: Document Data Extraction;
:heavy_check_mark: Document Classification;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python]()
- [Docker]()
- [Pytorch Lightning]()
- [Hugging Face]()
- [EasyOCR]()
- [Streamlit]()
- [Jupyter]()

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git]() or [Docker]() installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/human-ai2025/document_ocr_classification

# Access
$ cd document_ocr_classification
#
# For devlopment 
docker compose -f build_run\deploy\docker-compose-dev.yaml down && docker build -f dev.Dockerfile -t pytorch_doc_ocr_classification_deploy:latest . && docker compose -f build_run\deploy\docker-compose-dev.yaml up

# For testing inferencing in bash mode
docker compose -f build_run\deploy\docker-compose-deploy-bash.yaml down && docker build -f deploy.Dockerfile -t pytorch_doc_ocr_classification_deploy:latest . && docker compose -f build_run\deploy\docker-compose-deploy-bash.yaml up -d
docker exec -it deploy-document-classification-1 bash


#For Inferencing (This is the part you need)
$ docker compose -f build_run\deploy\docker-compose-deploy.yaml down && docker build -f deploy.Dockerfile -t pytorch_doc_ocr_classification_deploy:latest . && docker compose -f build_run\deploy\docker-compose-deploy.yaml up

# Locally in windows/Mac machine most probably EOL error may come dur to the script file 
#Change the EOL of startup.sh in build_run/deploy to overcome those issues 
# Now visit  http://localhost:8501/ in your browser 

# NOTES
# For interactive bash include the folllowing lines in docker compose under your service 
tty: true
stdin_open: true
command: sh

# To get the list versions only in pip 
pip3 list --format=freeze > requirements.txt

# To run stramlit 
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
View @ http://localhost:8501/
# The server will initialize in the <>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/human-ai2025" target="_blank">human-ai2025</a>

&#xa0;

<a href="#top">Back to top</a>
