# 🚀 MLOps Pipeline

> **From data to deployment — a simple, practical MLOps pipeline built from scratch.**

A personal project exploring how a machine learning model moves beyond a notebook and into a reproducible, trackable, and deployable workflow.

This project uses the **Iris dataset** as a lightweight example to demonstrate an end-to-end ML lifecycle — from data preparation and model training to experiment tracking, API serving, containerization, and CI/CD automation.

---

## 🧠 What This Project Demonstrates

Machine learning isn't just about training a model.

A useful ML system also needs a reliable way to:

**Prepare data → Train → Track experiments → Save the model → Serve predictions → Automate the workflow**

That's what this project is designed to demonstrate.

### Pipeline

```text
                ┌─────────────────┐
                │   Iris Dataset  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Data Pipeline  │
                │  prepare_data   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Model Training  │
                │ Random Forest   │
                └────────┬────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       ┌─────────────┐       ┌─────────────┐
       │   MLflow    │       │  model.pkl  │
       │ Experiments │       │    Model    │
       └─────────────┘       └──────┬──────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │   FastAPI API   │
                           │    /predict     │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │     Docker      │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │ GitHub Actions  │
                           │     CI/CD       │
                           └─────────────────┘
```

---

## ✨ Features

* 🌱 **Automated data preparation** using the Iris dataset
* 🤖 **Random Forest classification** for model training
* 📊 **Experiment tracking with MLflow**
* 📦 **Model serialization** using Joblib
* ⚡ **FastAPI inference API**
* 🐳 **Dockerized application**
* 🔄 **GitHub Actions CI/CD pipeline**
* 💾 **DVC integration** for data/version management
* 🧩 Simple and modular project structure

---

## 🛠️ Tech Stack

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| 🐍 Python         | Core development                    |
| 🐼 Pandas         | Data processing                     |
| 🧠 Scikit-learn   | Machine learning                    |
| 📈 MLflow         | Experiment tracking & model logging |
| ⚡ FastAPI         | Model serving                       |
| 🚀 Uvicorn        | ASGI server                         |
| 🐳 Docker         | Containerization                    |
| 🔄 GitHub Actions | CI/CD automation                    |
| 📦 DVC            | Data versioning                     |
| 🔧 Joblib         | Model serialization                 |

---

## 📁 Project Structure

```text
MLOps-Pipeline/
│
├── .dvc/                    # DVC configuration
├── .github/
│   └── workflows/
│       └── deploy.yml       # CI/CD workflow
│
├── data/
│   └── iris.csv             # Prepared dataset
│
├── src/
│   ├── prepare_data.py      # Data preparation
│   ├── train.py             # Model training & MLflow tracking
│   └── app.py               # FastAPI inference service
│
├── mlruns/                  # MLflow experiment artifacts
├── mlflow.db                # MLflow tracking database
├── model.pkl                # Trained model
├── dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔄 How It Works

### 1. Data Preparation

The pipeline starts by loading the built-in **Iris dataset** from Scikit-learn and converting it into a structured CSV file.

```bash
python src/prepare_data.py
```

This creates:

```text
data/iris.csv
```

The dataset contains the four flower measurements used for classification:

* Sepal length
* Sepal width
* Petal length
* Petal width

---

### 2. Model Training

The training pipeline loads the prepared dataset and trains a **Random Forest Classifier**.

```bash
python src/train.py
```

The training process:

1. Loads the dataset
2. Splits data into training and testing sets
3. Creates a Random Forest model
4. Trains the model
5. Evaluates accuracy
6. Logs parameters and metrics to MLflow
7. Saves the trained model as `model.pkl`

The current experiment tracks parameters such as:

```text
n_estimators = 100
max_depth    = 5
```

MLflow is used to record the experiment and model information.

---

## 📊 Experiment Tracking with MLflow

MLflow makes it possible to keep track of model experiments instead of relying on scattered notebooks or manual notes.

The project creates an experiment called:

```text
iris_classification
```

Tracked information includes:

* Model hyperparameters
* Accuracy
* Trained model artifact

This provides a foundation for comparing experiments and managing model iterations.

---

## ⚡ FastAPI Model Serving

Once the model has been trained, it can be exposed through a REST API.

Start the API with:

```bash
uvicorn src.app:app --reload
```

The API provides:

### Health / Home

```http
GET /
```

### Prediction

```http
POST /predict
```

Example request:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example response:

```json
{
  "prediction": 0
}
```

FastAPI also provides interactive API documentation at:

```text
http://localhost:8000/docs
```

The `/predict` endpoint accepts the four Iris measurements and uses the saved model to generate a prediction.

---

## 🐳 Running with Docker

The application includes a Docker configuration based on Python 3.9.

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

Interactive Swagger documentation:

```text
http://localhost:8000/docs
```

The container exposes port `8000` and starts the FastAPI application using Uvicorn.

---

## 🔄 CI/CD with GitHub Actions

The project also includes a GitHub Actions workflow that runs when changes are pushed to the `main` branch.

The workflow currently:

```text
Push to main
     │
     ▼
Checkout repository
     │
     ▼
Setup Python 3.9
     │
     ▼
Install dependencies
     │
     ▼
Prepare data
     │
     ▼
Train model
```

This helps automate the ML workflow and ensures that the data preparation and training steps can be reproduced in CI.

---

## 💻 Getting Started

### Prerequisites

Make sure you have:

* Python 3.9+
* Git
* Docker *(optional)*
* DVC *(optional, depending on your workflow)*

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

---

## 🧪 Example Workflow

A complete local run looks like this:

```bash
# 1. Prepare data
python src/prepare_data.py

# 2. Train and track the model
python src/train.py

# 3. Start the API
uvicorn src.app:app --reload
```

Then test the prediction endpoint through the Swagger UI:

```text
http://localhost:8000/docs
```

---

## 🎯 Why I Built This

This project was built as a hands-on exploration of **MLOps concepts** and the transition from a traditional machine learning workflow to a more automated engineering workflow.

The goal wasn't to build the most complex ML model.

Instead, I wanted to understand the pieces that surround a model:

> **How do we prepare data consistently?**
> **How do we track experiments?**
> **How do we package a trained model?**
> **How do we expose it as an API?**
> **How do we automate the workflow?**

Using a small dataset keeps the ML problem simple so the focus stays on the **ML engineering and MLOps workflow**.

---

## 🚧 Future Improvements

This project is intentionally lightweight and serves as a foundation for further experimentation.

Potential improvements include:

* [ ] Add automated unit & integration tests
* [ ] Add model validation gates
* [ ] Add model versioning through a model registry
* [ ] Improve DVC-based data pipeline integration
* [ ] Add automated Docker image builds
* [ ] Push images to a container registry
* [ ] Add cloud deployment
* [ ] Add model monitoring
* [ ] Add data/model drift detection
* [ ] Add automated retraining
* [ ] Add proper CI/CD deployment stages
* [ ] Add API authentication and production configuration

---

## 📌 Current Scope

This is a **personal learning project** focused on understanding the fundamentals of an end-to-end MLOps workflow.

The ML problem itself is intentionally simple; the interesting part is the engineering around it.

**Data → ML → Tracking → API → Container → Automation**

---

## ⭐ If You Find It Useful

Feel free to explore the repository, experiment with the pipeline, or use it as a starting point for your own MLOps projects.

If you found it useful, consider giving the repository a ⭐.

**Built with curiosity, Python, and a little bit of MLOps. 🚀**

---

### 🔗 Repository

[View MLOps-Pipeline on GitHub](https://github.com/Parthnvm/MLOps-Pipeline?utm_source=chatgpt.com)
