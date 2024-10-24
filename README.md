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

```bash
git clone https://github.com/julescrevola/xhec-mlops-project-student
cd <repository-directory>
```

### 2. Set Up the Python Environment

**Using conda**

- Install the app dependencies by running the following command:
```bash
pip-compile requirements.in
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
