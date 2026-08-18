# MLOps Pipeline

An end-to-end machine learning pipeline built to explore practical MLOps concepts — from data preparation and model training to experiment tracking, API serving, containerization, and CI/CD.

## Overview

This project uses the **Iris dataset** to demonstrate a simple but complete ML workflow.

The focus is not on the complexity of the model, but on understanding the engineering practices around building and deploying machine learning systems.

```text
Data → Training → Experiment Tracking → Model → API → Docker → CI/CD
```

## Tech Stack

* **Python** — Core development
* **Scikit-learn** — Model training
* **Pandas** — Data processing
* **MLflow** — Experiment tracking
* **FastAPI** — Model serving
* **Docker** — Containerization
* **GitHub Actions** — CI/CD
* **DVC** — Data versioning
* **Joblib** — Model serialization

## Project Structure

```text
MLOps-Pipeline/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── data/
│   └── iris.csv
│
├── src/
│   ├── prepare_data.py
│   ├── train.py
│   └── app.py
│
├── mlruns/
├── model.pkl
├── dockerfile
├── requirements.txt
└── README.md
```

## Pipeline

### 1. Data Preparation

The Iris dataset is prepared and saved as a CSV file.

```bash
python src/prepare_data.py
```

### 2. Model Training

A Random Forest classifier is trained using the prepared dataset.

```bash
python src/train.py
```

The training process includes:

* Dataset loading and preprocessing
* Train/test split
* Random Forest training
* Model evaluation
* Experiment logging with MLflow
* Model serialization

The trained model is saved as:

```text
model.pkl
```

### 3. Experiment Tracking

MLflow is used to track model experiments, including parameters, metrics, and model artifacts.

The project uses an `iris_classification` experiment to keep track of training runs.

### 4. API

The trained model is exposed through a FastAPI application.

Start the API with:

```bash
uvicorn src.app:app --reload
```

Once running, the API documentation is available at:

```text
http://localhost:8000/docs
```

The prediction endpoint accepts the four Iris features:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### 5. Docker

The application can be packaged and run using Docker.

Build the image:

```bash
docker build -t mlops-pipeline -f dockerfile .
```

Run the container:

```bash
docker run -p 8000:8000 mlops-pipeline
```

The API will then be available at:

```text
http://localhost:8000
```

### 6. CI/CD

GitHub Actions is used to automate parts of the ML workflow when changes are pushed to the repository.

The workflow currently handles:

```text
Checkout
   ↓
Setup Python
   ↓
Install Dependencies
   ↓
Prepare Data
   ↓
Train Model
```

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Parthnvm/MLOps-Pipeline.git
cd MLOps-Pipeline
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the pipeline

```bash
python src/prepare_data.py
python src/train.py
```

### Start the API

```bash
uvicorn src.app:app --reload
```

Then open:

```text
http://localhost:8000/docs
```

## Project Goals

This project was built as a hands-on way to understand how a machine learning model can move from a local training script toward a more structured and reproducible workflow.

The main areas explored are:

* Data preparation
* Model training
* Experiment tracking
* Model serialization
* API-based inference
* Containerization
* CI/CD automation

## Future Improvements

* Add automated tests
* Improve data and model versioning
* Add model validation
* Add a model registry
* Automate Docker image builds
* Add cloud deployment
* Add model and data drift monitoring
* Add automated retraining

## Author

**Parth**

This is a personal project built to learn and experiment with practical MLOps workflows.

[GitHub Repository](https://github.com/Parthnvm/MLOps-Pipeline)
