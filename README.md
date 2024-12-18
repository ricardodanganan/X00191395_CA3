# X00191395_CA3
## GitHub Repository Setup

To meet submission requirements for CA3, the following steps were taken to create and configure the GitHub repository:

### Repository Creation
- A new repository named `X00191395_CA3` was created on GitHub.
- The repository was initialized with a `README.md` file and set to **Private**.

### Adding Collaborator
- The lecturer, Mr. Damian Niezgoda, was added as a collaborator with **Maintain/Admin** privileges.

### Repository Cloning
- The repository was cloned locally to `C:/College - DevOps_Projects/X00191395_CA3`.

#### Screenshots:
![GitHub Repository Screenshot](images/Github-repo-page.jpg)

## Azure DevOps Project Setup

To meet submission requirements, the Azure DevOps project was created and configured as follows:

### Project Creation
- A new Azure DevOps project named `X00191395_CA3` was created.
- The project visibility was set to **Private**.

### Adding Project Administrator
- The lecturer, Mr. Damian Niezgoda, was added as a Project Administrator.

#### Screenshots:
![Azure DevOps Project Screenshot](images/Azure-creation-page.jpg)

## Branch Management Strategy

To follow best practices in source control, the following branches were created:

1. **Main Branch**:
   - The production-ready branch that contains stable code.
   - All changes are reviewed and tested before being merged here.

2. **Development Branch**:
   - The working branch where new features and fixes are developed.
   - Changes are tested here before being merged into the main branch.

### Steps to Create the Development Branch
1. Checked out the main branch:
   ```bash
   git checkout main

2. Created and switched to the development branch:
   ```bash
   git checkout -b development

3. Pushed the branch to GitHub:
   ```bash
   git push -u origin development

#### Screenshots:
![Github Development Branch](images/Github-development-branch.jpg)

## CI/CD Pipeline Implementation

### Multi-Stage Pipeline
The CI/CD pipeline for this project was implemented using Azure DevOps. The pipeline is configured as follows:

1. **Build Stage**:
   - Installs dependencies and builds the project.
   - Publishes build artifacts for deployment.

2. **Deployment Stages**:
   - **Test Environment**:
     - Deploys the application to a test environment for validation.
   - **Production Environment**:
     - Deploys the application to the production environment after manual approval.

### Pipeline Configuration
The pipeline is defined in a YAML file (`azure-pipelines.yml`) with the following stages:
- Build
- Deploy to Test
- Deploy to Production

### Approval Gates
- Manual approval is required before deployment to the production environment.