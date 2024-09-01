# MLOPS_project-1

# Gemstone Price Prediction

An end-to-end machine learning pipeline for predicting gemstone prices, deployed on Azure.

## Overview

This project involves:
- **Data Ingestion & Preprocessing:** Handling and preparing data for model training.
- **Model Training & Evaluation:** Building and assessing the predictive model.
- **API Deployment:** Providing a Flask-based web interface for predictions.
- **Azure Deployment:** Containerized deployment using Docker and automated CI/CD via GitHub Actions.

## Project Structure

├── src │ ├── components │ │ ├── data_ingestion.py │ │ ├── data_preprocessing.py │ │ ├── model_training.py │ │ ├── model_evaluation.py │ ├── pipelines │ │ ├── training_pipeline.py │ │ ├── inference_pipeline.py │ ├── app.py │ ├── templates │ ├── index.html │ ├── result.html ├── Dockerfile ├── requirements.txt ├── dvc.yaml ├── .github │ ├── workflows │ ├── azure.yml ├── README.md


## Setup & Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/HARIMANOJ05/MLOPS_project-1.git
    cd MLOPS_project-1
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application Locally:**
    ```bash
    python src/app.py
    ```

## Deployment

The project is deployed on Azure using GitHub Actions. The deployment workflow is defined in `.github/workflows/azure.yml` and involves:

1. **Building & Pushing Docker Image:**
   - The Dockerfile builds the application container.
   - The image is pushed to Azure Container Registry.

2. **Deploying to Azure Web App:**
   - The container is deployed to Azure Web App using the publish profile and credentials.

## Usage

Access the application via the Azure Web App URL. Use the web interface to input gemstone features and receive price predictions.

## Contributing

Contributions are welcome. Please submit issues or pull requests for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For detailed setup instructions and additional configuration, refer to the project's documentation and configuration files.
