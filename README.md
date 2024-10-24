<div align="center">

# xhec-mlops-project-student

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: flake8](https://img.shields.io/badge/code%20style-flake8-blue)](https://github.com/PyCQA/flake8)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

## Contributors

| Name                     | Email                                      |
|--------------------------|--------------------------------------------|
| [Jules Crevola](mailto:julescrevola@email.com)       | julescrevola@email.com           |
| [Ghali Chraibi](mailto:ghali.chraibi@polytechnique.edu) | ghali.chraibi@polytechnique.edu  |
| [Carlo Antonio Patti](mailto:carlopatti1@gmail.com)  | carlopatti1@gmail.com            |
| [Mohamed Benslimane](mailto:benslimane15.mohamed@gmail.com) | benslimane15.mohamed@gmail.com   |
| [Antonio Roberto Ventura](mailto:antonio.ventu@hotmail.com) | antonio.ventu@hotmail.com        |

## Description

## Contributors

| Name                     | Email                                      |
|--------------------------|--------------------------------------------|
| [Jules Crevola](mailto:julescrevola@email.com)       | julescrevola@email.com           |
| [Ghali Chraibi](mailto:ghali.chraibi@polytechnique.edu) | ghali.chraibi@polytechnique.edu  |
| [Carlo Antonio Patti](mailto:carlopatti1@gmail.com)  | carlopatti1@gmail.com            |
| [Mohamed Benslimane](mailto:benslimane15.mohamed@gmail.com) | benslimane15.mohamed@gmail.com   |
| [Antonio Roberto Ventura](mailto:antonio.ventu@hotmail.com) | antonio.ventu@hotmail.com        |

## Description

This repository has for purpose to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.

<details>
<summary>Details on the Abalone Dataset</summary>

The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)

You can download the dataset on the [Kaggle page](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset)

</details>

## Table of Contents

- [xhec-mlops-project-student](#xhec-mlops-project-student)
  - [Table of Contents](#table-of-contents)
  - [Deliverables and Evaluation](#deliverables-and-evaluation)
    - [Deliverables](#deliverables)
    - [Evaluation](#evaluation)
  - [Steps to reproduce to build the deliverable](#steps-to-reproduce-to-build-the-deliverable)
    - [Pull requests in this project](#pull-requests-in-this-project)
    - [Tips to work on this project](#tips-to-work-on-this-project)

# Environment Setup

This section outlines the steps to set up the Python environment for this project.

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **pip** (Python package installer)
- (Optional) **conda** (if you are using it to manage environments)
- **pre-commit** (for running pre-commit hooks)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:
# Environment Setup

This section outlines the steps to set up the Python environment for this project.

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **pip** (Python package installer)
- (Optional) **conda** (if you are using it to manage environments)
- **pre-commit** (for running pre-commit hooks)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/julescrevola/xhec-mlops-project-student
cd <repository-directory>
```

### 2. Set Up the Python Environment

**Option 1: Using pip**

- Install the app dependencies by running the following command:
```bash
pip install -r requirements.txt
```

- If you are contributing to the development of this project, install the development dependencies:
```bash
pip install -r requirements-dev.txt
```

**Option 2: Using conda**

- If you're using conda, create and activate a new environment from the environment.yml
```bash
conda env create -f environment.yml
conda activate <env_name>
```

**Option for dev-only: Setup Pre-commit Hooks**

To ensure code quality and enforce coding standards, the project uses pre-commit hooks:

Install the pre-commit hooks defined in ```pre-commit-config.yaml```
```bash
pre-commit install
```

- If you are contributing to the development of this project, install the development dependencies:
```bash
pip-compile requirements-dev.in
```

- If you're using conda, create and activate a new environment from the environment.yml
```bash
conda env create -f environment.yml
conda activate <env_name>
```

- If you need to update the environment after having compiled the requirements with new packages, you can run
```bash
conda env update -f environment.yml --prune
conda activate <env_name>
```

**Option for dev-only: Setup Pre-commit Hooks**

To ensure code quality and enforce coding standards, the project uses pre-commit hooks:

Install the pre-commit hooks defined in ```pre-commit-config.yaml```
```bash
pre-commit install
```

### 3. Downloading the Dataset
To download the dataset for this project, you will need to use the opendatasets library. Follow these steps:

**Kaggle Account:**

You must have a Kaggle account. If you don’t have one, you can sign up at Kaggle.

**Create Kaggle API Token**

Go to your Kaggle account settings by clicking on your profile picture in the top right corner and selecting "Account".
Scroll down to the "API" section and click on the "Create New API Token" button. This will download a file named kaggle.json.
Setting Up Your Environment

**Place the kaggle.json File:**

Move the downloaded kaggle.json file to the appropriate directory ~/src/modelling

# FastAPI Model Service

## Usage

### Running the FastAPI Application

Make sure your pre-trained model and preprocessor files are in the correct directory:
```
web_service/local_objects/random_forest.pkl
web_service/local_objects/preprocessor.pkl
```

Run the FastAPI application:
```bash
uvicorn main:app --reload
```

This command will start the server, and you can access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Making Predictions

You can make predictions by sending a POST request to the `/predict` endpoint. You can use tools like Postman, cURL, or Python's requests library.

#### Example Request

Here’s how to send a POST request with sample data:

Using cURL:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
    "Length": 0.455,
    "Diameter": 0.365,
    "Height": 0.095,
    "Whole_weight": 0.514,
    "Shucked_weight": 0.224,
    "Viscera_weight": 0.101,
    "Shell_weight": 0.150,
    "Sex": "M"
}'
```

## Building and Running with Docker

### Building the Docker Image

To build the Docker image, ensure you are in the root directory of the project (where the `Dockerfile` is located) and run the following command:

```bash
docker build -t fastapi-model-service .
```

This command will create a Docker image named `fastapi-model-service`.

### Running the Docker Container

Once the image is built, you can run a container from the image using the following command:

```bash
docker run -d -p 8000:8000 fastapi-model-service
```

This will start a container and map port `8000` on your host to port `8000` in the container. You can now access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Stopping the Container

To stop the running container, first find its container ID:

```bash
docker ps
```

Then stop it using:

```bash
docker stop <container_id>
```

Replace `<container_id>` with the actual container ID.
