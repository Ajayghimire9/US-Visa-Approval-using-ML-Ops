# US-Visa-Approval-using-ML-Ops

This project aims to predict US Visa approval using advanced Machine Learning operations (MLOps). It integrates a comprehensive workflow that spans constant definition, configuration management, artifact handling, modular component implementation, pipeline execution, and a user interface for application interaction.

## Environment Setup

Begin by setting up your environment to ensure all dependencies are correctly installed:

### Create and Activate Conda Environment

```bash
# Create a new Conda environment named 'visa' with Python 3.8
conda create -n visa python=3.8 -y

# Activate the 'visa' environment
conda activate visa

### Install Required Dependencies

```bash
# Install required Python packages from requirements.txt
pip install -r requirements.txt

Project Workflow
The project is organized into key components for efficient workflow management:

Constants: Central definitions for consistent use across the project.
Config Entity: Configuration entities that encapsulate the required setups.
Artifact Entity: Management of generated artifacts, such as data files, models, and logs.
Components: Specific tasks within the pipeline, including data ingestion, preprocessing, model training, and others.
Pipeline: The orchestration layer that manages the flow of data through the components and executes the machine learning pipeline.
Application Interface (app.py): The entry point for running the pipeline, facilitating user interaction and control.
Running the Application
After setting up your environment and installing all dependencies, initiate the project by running the application interface:

bash
Copy code
# Execute the application script
python app.py
This command triggers the execution of the machine learning pipeline, processing the input data, training the model on it, and evaluating its performance to provide insights into the US visa approval prediction process.
