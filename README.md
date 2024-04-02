# US Visa Approval Prediction using Advanced MLOps

This project aims to predict US Visa approval using advanced Machine Learning operations (MLOps). It integrates a comprehensive workflow that spans constant definition, configuration management, artifact handling, modular component implementation, pipeline execution, and a user interface for application interaction.

## Environment Setup

Begin by setting up your environment to ensure all dependencies are correctly installed:

### Create and Activate Conda Environment

conda create -n visa python=3.8 -y
conda activate visa


### Install Required Dependencies


pip install -r requirements.txt


## Project Workflow

The project is organized into key components for efficient workflow management:

- Constants: Different variables
- Config Entity: all files paths
- Artifact Entity: data files 
- Components: acutal stage 
- Pipeline: The orchestration layer that manages the flow of data through the components and executes the machine learning pipeline.
- Application Interface (`app.py`): The entry point for running the pipeline, facilitating user interaction and control.

## Running the Application

After setting up your environment and installing all dependencies, initiate the project by running the application interface:

python app.py
