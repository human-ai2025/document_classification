<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Document_classification" />

  &#xa0;

  <!-- <a href="https://document_classification.netlify.app">Demo</a> -->
</div>

<h1 align="center">Document Ocr Classification</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/document_classification?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/document_classification?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/document_classification?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/document_classification?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/document_classification?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/document_classification?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/document_classification?color=56BEB8" /> -->
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
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Describe your project

## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##

The following tools were used in this project:

- [Expo](https://expo.io/)
- [Node.js](https://nodejs.org/en/)
- [React](https://pt-br.reactjs.org/)
- [React Native](https://reactnative.dev/)
- [TypeScript](https://www.typescriptlang.org/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Node](https://nodejs.org/en/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/human-ai2025/document_ocr_classification

# Access
$ cd document_ocr_classification

# For devlopment 
docker compose -f build_run\deploy\docker-compose-dev.yaml down && docker build -f dev.Dockerfile -t pytorch_doc_ocr_classification_deploy:latest . && docker compose -f build_run\deploy\docker-compose-dev.yaml up

#For Inferencing
$ docker compose -f build_run\deploy\docker-compose-deploy-bash.yaml down && docker build -f deploy.Dockerfile -t pytorch_doc_ocr_classification_deploy:latest . && docker compose -f build_run\deploy\docker-compose-deploy-bash.yaml up

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


Made with :heart: by <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">{{YOUR_NAME}}</a>

&#xa0;

<a href="#top">Back to top</a>
