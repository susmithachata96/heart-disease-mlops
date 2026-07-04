# ❤️ Heart Disease Prediction using MLOps

A production-ready MLOps project for predicting the presence of heart disease using the UCI Heart Disease dataset. This repository demonstrates an end-to-end machine learning workflow covering data preprocessing, exploratory data analysis, model training, experiment tracking, API deployment, containerization, CI/CD automation, Kubernetes deployment, monitoring, and documentation.

---
## Project Status

- [x] Project Initialization
- [ ] Data Acquisition
- [ ] Exploratory Data Analysis
- [ ] Feature Engineering
- [ ] Model Training
- [ ] MLflow Integration
- [ ] FastAPI Development
- [ ] Docker Containerization
- [ ] CI/CD Pipeline
- [ ] Kubernetes Deployment
- [ ] Monitoring
- [ ] Final Report

---

## 1. Project Overview

Heart Disease Prediction using MLOps is designed to showcase how machine learning models can be built, packaged, deployed, and monitored using modern MLOps practices. The project combines data science workflows with DevOps principles to create a reliable, reproducible, and scalable solution for healthcare prediction.

The repository is structured to help developers and data scientists understand how to move from experimentation to production in a systematic and professional way.

---

## 2. Project Workflow

Dataset
      │
      ▼
EDA & Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
MLflow Experiment Tracking
      │
      ▼
Model Serialization
      │
      ▼
FastAPI
      │   
      ▼
Docker
      │
      ▼
GitHub Actions
      │
      ▼
Kubernetes
      │
      ▼
Monitoring

---

## 3. Objectives

- Build a reliable machine learning pipeline for heart disease prediction.
- Demonstrate end-to-end MLOps practices from data ingestion to deployment.
- Track experiments and model versions in a reproducible manner.
- Expose the trained model through a REST API.
- Containerize the application for portability and scalability.
- Implement CI/CD and deployment automation.
- Provide a clear documentation foundation for collaboration and maintainability.

---

## 4. Features

- Data preprocessing and feature engineering.
- Exploratory data analysis (EDA) and visualization.
- Model training and evaluation.
- Experiment tracking with tools such as MLflow or Weights & Biases.
- FastAPI-based prediction service.
- Docker support for containerized deployment.
- CI/CD pipelines for automated testing and deployment.
- Kubernetes deployment manifests.
- Monitoring and logging support.
- Well-documented project structure for reuse and extension.

---

## 5. Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost (if used) |
| Experiment Tracking | MLflow |
| API Development | FastAPI, Uvicorn |
| Containerization | Docker |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Testing | Pytest |
| Environment Management | Virtualenv / Conda |

---

## 6. Project Directory Structure

```text
heart-disease-mlops/
├── data/                    # Dataset and processed data
├── deployment/              # Deployment manifests and scripts
├── docs/                    # Project documentation
├── models/                  # Trained model artifacts
├── notebooks/               # Jupyter notebooks for EDA and experimentation
├── screenshots/             # Screenshots and visuals
├── src/                     # Source code for training and inference
├── tests/                   # Unit and integration tests
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container definition
├── docker-compose.yml       # Optional local orchestration config
└── README.md                # Project documentation
```

---

## 7. Installation Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd heart-disease-mlops
```

2. Create and activate a virtual environment.

3. Install dependencies.

4. Run the notebook, train the model, and start the API server.

---

## 8. Creating and Activating Virtual Environment

### On Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### On macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Replace the commands above with your preferred environment manager if needed.

---

## 9. Installing Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

If dependencies are managed separately, use:

```bash
pip install <package-name>
```

---

## 10. Running Jupyter Notebook

Start Jupyter Notebook with:

```bash
jupyter notebook
```

Or use:

```bash
jupyter lab
```

The notebooks for data exploration and model experimentation can be found in the [notebooks](notebooks) directory.

---

## 11. Training the Model

Run the training script from the project root:

If the training workflow is organized differently, replace the command above with the appropriate entry point.

---

## 12. Running the FastAPI Server

Start the API server locally with:

```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

You can then access the API documentation at:

- http://localhost:8000/docs
- http://localhost:8000/redoc

---

## 13. Docker Instructions

Build the Docker image:

```bash
docker build -t heart-disease-mlops .
```

Run the container:

```bash
docker run -p 8000:8000 heart-disease-mlops
```

Additional Docker commands can be added here as the deployment workflow evolves.

---

## 14. CI/CD Workflow

This repository is intended to support continuous integration and continuous deployment through GitHub Actions.

Suggested workflow:

1. Run unit tests on every push and pull request.
2. Build the Docker image.
3. Deploy the application to a staging or production environment.
4. Validate logs and health checks after deployment.

Example placeholder:

```yaml
# Add GitHub Actions workflow here
```

---

## 15. Kubernetes Deployment

Deployment manifests can be added under the [deployment](deployment) directory.

Example deployment steps:

```bash
kubectl apply -f deployment/
```

Additional resources such as Service, Ingress, ConfigMap, and Secret manifests should be added as the project matures.

---

## 16. Monitoring

Monitoring is essential for maintaining model performance and service reliability.

Recommended monitoring practices include:

- Application logs and structured error tracking.
- Performance metrics for API latency and request volume.
- Model drift and prediction quality monitoring.
- Health checks for the deployment environment.

Add monitoring tools and dashboards in this section as they are implemented.

---

## 17. Future Enhancements

- Add automated model retraining pipelines.
- Improve model interpretability with explainability tools.
- Add support for model versioning and rollback.
- Expand monitoring with drift detection and alerting.
- Integrate with cloud-native deployment platforms.
- Improve test coverage and production readiness.

---

## 18. Author

Name: Susmitha Chatakondu

Role: Machine Learning Engineer / MLOps Engineer

Email: 2024ac05616@wilp.bits-pilani.ac.in

GitHub: https://github.com/your-username

---

## License

This project is intended for educational and professional demonstration purposes. Add your preferred license file and license details here.
