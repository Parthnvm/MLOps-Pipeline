import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import joblib
mlflow.sklearn.autolog()

# 1. Load Data
df = pd.read_csv('data/iris.csv')
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Start MLflow Experiment
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("iris_classification")

with mlflow.start_run():
    # Hyperparameters
    n_estimators = 100
    max_depth = 5
    
    # Train Model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X_train, y_train)
    
    # Evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    # Log parameters and metrics
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", accuracy)
    
    # Save the model locally for our API
    joblib.dump(model, 'model.pkl')
    mlflow.sklearn.log_model(model, "model")
    
    print(f"Model trained with accuracy: {accuracy}")