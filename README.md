# US-Visa-Approval-Prediction

This project aims to predict the approval status of US Visa applications using machine learning models. It demonstrates the application's workflow from data processing to model prediction, integrating various technologies, including MongoDB for database management, AWS for cloud services, and Docker for containerization.


## Quickstart

### Prerequisites

- Anaconda or Miniconda
- Git

### Environment Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ajayghimire9/US-Visa-Approval-using-ML-Ops
    cd US-Visa-Approval-Prediction
    ```

2. **Create and activate a new Conda environment:**

    ```bash
    conda create -n visa python=3.8 -y
    conda activate visa
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Replace `<username>`, `<password>`, `<AWS_ACCESS_KEY_ID>`, and `<AWS_SECRET_ACCESS_KEY>` with your actual credentials.

    ```bash
    export MONGODB_URL="mongodb+srv://<username>:<password>@..."
    export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
    export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

## Workflow Overview

The application follows a structured pipeline for processing and predicting US Visa approval status:

1. **Constant:** Defines constant values used across the project.
2. **Config Entity:** Manages configuration entities for the project.
3. **Artifact Entity:** Handles the artifacts generated during the project.
4. **Component:** Core components including data processing, modeling, etc.
5. **Pipeline:** Orchestrates the workflow from data to prediction.
6. **App/Demo:** The main application script for launching the project.

## Git Commands

Basic Git commands to track changes and push updates to the repository:

```bash
git add .
git commit -m "Updated"
git push origin main


## AWS CI/CD Deployment with GitHub Actions

Automate the deployment process using GitHub Actions for continuous integration and continuous deployment (CI/CD) with AWS services.

### Setting up AWS

Before starting with GitHub Actions, set up the necessary AWS resources and permissions.

1. **Login to AWS Console:**
   - Navigate to the AWS Management Console and log in with your credentials.

2. **Create an IAM user:**
   - Go to the IAM dashboard and create a new user.
   - Grant the following access permissions:
     - EC2 Access: Allows management of EC2 instances.
     - ECR Access: Permission to push and pull from Elastic Container Registry.

3. **Attach Policies:**
   - Attach the following policies to the user for the required permissions:
     - `AmazonEC2ContainerRegistryFullAccess`
     - `AmazonEC2FullAccess`

### Deployment Steps

Follow these steps to prepare and execute the deployment:

1. **Create an ECR Repository:**
   - In the AWS Management Console, navigate to the ECR service and create a new repository.
   - Note the repository's URI for later steps.

2. **Launch an EC2 Instance:**
   - Create a new EC2 instance, selecting Ubuntu as the recommended OS.
   - After launch, connect to your instance and install Docker:
     ```bash
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh
     sudo usermod -aG docker $USER
     ```

3. **Configure EC2 as a Self-hosted Runner:**
   - In your GitHub repository, go to Settings > Actions > Runners.
   - Click on "New runner" and select the appropriate OS.
   - Follow the instructions to configure your EC2 instance as a self-hosted runner.

4. **Setup GitHub Secrets:**
   - In your repository settings, navigate to Secrets and add the following:
     - `AWS_ACCESS_KEY_ID`: Your IAM user's access key.
     - `AWS_SECRET_ACCESS_KEY`: Your IAM user's secret access key.
     - `AWS_DEFAULT_REGION`: Your AWS region.
     - `ECR_REPO`: The URI of your ECR repository.

### Automating Deployment with GitHub Actions

- Create a `.github/workflows/aws-deployment.yml` file in your repository.
- Define the steps for building your Docker image, pushing it to ECR, and deploying it to EC2.

### Conclusion

This project demonstrates an end-to-end machine learning application, from data processing and model training to deployment using AWS and GitHub Actions. It showcases how to leverage cloud services and CI/CD pipelines for efficient deployment workflows.

For contributions, issues, or further inquiries, consider opening an issue in the project's GitHub repository or contacting the project maintainers directly.
