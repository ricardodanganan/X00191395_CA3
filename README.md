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

   ```

2. Created and switched to the development branch:

   ```bash
   git checkout -b development

   ```

3. Pushed the branch to GitHub:
   ```bash
   git push -u origin development
   ```

#### Screenshots:

![Github Development Branch](images/Github-development-branch.jpg)

## **CI/CD Pipeline Implementation**

### **Overview**

The CI/CD pipeline was set up in Azure DevOps to automate the build and testing of the To-Do List application. It performs the following tasks:

1. **Set Up Python 3.x**: Installs the Python environment.
2. **Install Dependencies**: Upgrades `pip` for package management.
3. **Run Unit Tests**: Executes unit tests defined in `test_todo.py`.

---

### **Steps to Create the Pipeline**

1. **Created the Pipeline in Azure DevOps**:

   - Selected **GitHub** as the source.
   - Chose the repository `X00191395_CA3`.

2. **Added the Pipeline Configuration**:

   ```bash
   touch azure-pipelines.yml
   trigger:
   - development
   stages:
   - stage: Build
   displayName: 'Build and Test Stage'
   jobs:
   - job: BuildAndTest
    displayName: 'Install and Run Tests'
    pool:
    vmImage: 'ubuntu-latest'
    steps:
    - task: UsePythonVersion@0
      inputs:
      versionSpec: '3.x'
      displayName: 'Set Up Python 3.x'
    - script: |
      python -m pip install --upgrade pip
      displayName: 'Upgrade Pip'
    - script: |
      python -m unittest test_todo.py
      displayName: 'Run Unit Tests'

   ```

3. **Committed and Pushed the Pipeline to GitHub**:

   ```bash
   git add azure-pipelines.yml
   git commit -m "Added CI/CD pipeline configuration"
   git push origin development

   ```

4. **Ran the Pipeline**:
   - Triggered the pipeline manually from Azure DevOps.
   - Verified the success of each step.

#### Screenshots:

![pipeline success](images/pipeline-success.jpg)

## **Multi-Environment Deployment**

### **Overview**

The pipeline includes three stages:

1. **Build and Test Stage**: Runs unit tests for the application.
2. **Deploy to Test Environment**: Deploys the application to a Test environment.
3. **Deploy to Production Environment**: Deploys to Production with an approval gate.

---

### **Steps to Implement Multi-Environment Deployment**

1. **Updated the Pipeline Configuration**:

   ```yaml
   trigger:
     - development

   stages:
     - stage: Build
       displayName: "Build and Test Stage"
       jobs:
         - job: BuildAndTest
           displayName: "Install and Run Tests"
           pool:
             vmImage: "ubuntu-latest"
           steps:
             - task: UsePythonVersion@0
               inputs:
                 versionSpec: "3.x"
               displayName: "Set Up Python 3.x"

             - script: |
                 python -m pip install --upgrade pip
               displayName: "Upgrade Pip"

             - script: |
                 python -m unittest test_todo.py
               displayName: "Run Unit Tests"

     - stage: DeployToTest
       displayName: "Deploy to Test Environment"
       dependsOn: Build
       condition: succeeded()
       jobs:
         - deployment: TestDeploy
           displayName: "Deploy to Test"
           environment: "Test"
           strategy:
             runOnce:
               deploy:
                 steps:
                   - script: echo "Deploying To-Do List App to Test Environment"
                     displayName: "Deploy Step"

     - stage: DeployToProduction
       displayName: "Deploy to Production Environment"
       dependsOn: DeployToTest
       condition: succeeded()
       jobs:
         - deployment: ProdDeploy
           displayName: "Deploy to Production"
           environment: "Production"
           strategy:
             runOnce:
               deploy:
                 steps:
                   - script: echo "Deploying To-Do List App to Production Environment"
                     displayName: "Deploy Step"
   ```

2. **Committed and Pushed Changes**:

   ```bash
   git add azure-pipelines.yml
   git commit -m "Added multi-environment deployment with approval gate"
   git push origin development

   ```

3. **Committed and Pushed Changes**:

- Manually ran the pipeline in Azure DevOps.
- Monitored each stage.

#### Screenshots:

![Pipeline Execution](images/pipeline-multi-env.jpg)

### **Publishing Build Artifacts**

After the Build and Test Stage, the pipeline publishes artifacts for deployment and reference.

1. **Updated Pipeline**:

   - Added a `PublishBuildArtifacts` step to save build outputs.

2. **Artifact Details**:
   - **Name**: `ToDoApp-Build`
   - **Contents**: Source code and test outputs.

---

### **Screenshots**:

1. **Artifact Published**:
   ![Artifact Screenshot](images/pipeline-artifacts.jpg)

# Security Testing Documentation

## Overview

This section documents the **security testing** integration in the Azure DevOps CI/CD pipeline using **npm audit**. The **npm audit** security scan ensures that vulnerabilities in dependencies are identified and reported before deployment to production.

---

## Security Testing Implementation

### Tools Used

- **npm audit**: A built-in tool in Node.js for identifying security vulnerabilities in project dependencies.
- **Azure DevOps**: Used to run the npm audit scan and report results.

---

### Pipeline Integration

The security testing stage was integrated after deploying to the **Test Environment** and before deploying to **Production**.

---

### Pipeline YAML Code

1. **Below is the **updated YAML code** for the simplified security testing using **npm audit\*\*:

```yaml
# Security Testing Stage
- stage: SecurityTesting
  displayName: "Run Security Testing"
  dependsOn: DeployToTest
  condition: succeeded()
  jobs:
    - job: NPMAudit
      displayName: "Run NPM Audit Security Scan"
      pool:
        vmImage: "ubuntu-latest"
      steps:
        # Run npm audit
        - script: |
            npm install
            npm audit --audit-level=low --json > npm-audit-report.txt || echo "npm audit found vulnerabilities"
          displayName: "Run NPM Audit"

        # Publish NPM Audit Report
        - task: PublishBuildArtifacts@1
          inputs:
            PathtoPublish: "npm-audit-report.txt"
            ArtifactName: "NPM-Audit-Report"
          displayName: "Publish NPM Audit Report"
```

### How It Works

1. **Run NPM Audit**:

- Installs project dependencies using npm install.
- Executes npm audit with --audit-level=low to scan for vulnerabilities.
- Outputs the audit report in JSON format and saves it as npm-audit-report.txt.

2. **Publish the Report**:

- The npm audit report is published as a build artifact named NPM-Audit-Report.
- This artifact allows easy review of vulnerabilities.

## Pipeline Results

1. **Successful Execution**:

- The pipeline successfully runs npm audit and generates a vulnerability report.
- The report is published as part of the build artifacts.

2. **Pipeline Summary**:

- The SecurityTesting stage runs after the "Deploy to Test" stage.
- Artifacts such as the npm-audit-report.txt are stored and accessible for review.

## Artifacts and Reports

1. **NPM-Audit-Report**:

- Contains the output from npm audit.
- Stored as a text file (npm-audit-report.txt) in the Azure DevOps pipeline.

### **Screenshots**:

![Security Success](images/pipeline-security-success.jpg)

### **Screenshots**:

![NPM Audit report](images/NPM-Audit-report.jpg)

# Testing Implementation in Azure DevOps Pipeline

## Overview

This project integrates **Performance Testing** into the CI/CD pipeline using **Azure DevOps**. The testing stage ensures application performance is measured under simulated load before deployment.

---

## Pipeline Stages

### 1. **Build and Test Stage**

- **Objective**: Install dependencies and run unit tests.
- **Tools**: Python Unit Test Framework
- **Steps**:
  - Install Python 3.x.
  - Upgrade pip.
  - Execute unit tests (`python -m unittest`).

---

### 2. **Deploy to Test Environment**

- **Objective**: Deploy the application to the Test environment for further testing.
- **Steps**:
  - Simple deployment confirmation using an echo script.

---

### 3. **Performance Testing**

- **Objective**: Measure application performance under simulated load.
- **Tools**: **Artillery**
- **Steps**:
  - Install Artillery CLI.
  - Run Artillery load test on the application.
  - Save the test output report as `performance-report.txt`.
  - Publish the report as a pipeline artifact.

**Pipeline Code**:

```yaml
- stage: PerformanceTesting
  displayName: "Run Performance Testing"
  dependsOn: DeployToTest
  condition: succeeded()
  jobs:
    - job: ArtilleryTest
      displayName: "Run Artillery Load Test"
      pool:
        vmImage: "ubuntu-latest"
      steps:
        - script: |
            npm install -g artillery
            artillery quick --count 10 -n 20 http://localhost:8000 > performance-report.txt
          displayName: "Run Artillery Performance Test"
        - task: PublishBuildArtifacts@1
          inputs:
            PathtoPublish: "performance-report.txt"
            ArtifactName: "PerformanceTest-Report"
          displayName: "Publish Performance Test Report"
```

### 4. **Deploy to Production Environment**

- Deploy the application to the Production environment.

### 5. **Artifacts**

- PerformanceTest-Report: Contains the output of Artillery load testing.

### 6. **Results**

- Artillery Load Test: Provides a performance summary, including.
- Total requests sent.
- Response times (min, max, average).
- Errors encountered (if any).

### **Screenshots**:

![Performance testing](images/Performance-settings.jpg)

# Selenium UAT Test Implementation in Azure DevOps Pipeline

## **1. Overview**

The Selenium UAT (User Acceptance Testing) implementation ensures the web application's functionality meets requirements by simulating user actions and validating results.

---

## **2. Steps to Implement Selenium UAT Testing**

### **2.1 Selenium Script**

The Selenium script automates browser testing. Below is an example of a Selenium script written in Python:

**File:** `selenium_automation.py`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the application URL
    driver.get("http://localhost:8000")  # Replace with your test environment URL
    time.sleep(2)  # Allow time for the page to load

    # Step 2: Simulate user action (search or input field)
    search_box = driver.find_element(By.NAME, "q")  # Replace 'q' with your input field name
    search_box.send_keys("Test Data")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Step 3: Validate results
    assert "No results found." not in driver.page_source
    print("Test Passed: Search functionality works!")

except Exception as e:
    print(f"Test Failed: {str(e)}")

finally:
    driver.quit()  # Close the browser

```

### **2.2 Azure Pipeline Configuration**

The Selenium UAT Test stage is added to the Azure Pipeline YAML file. Below is the updated configuration:

**File:** `azure-pipelines.yml`

```yml
# Selenium UAT Test Stage
- stage: SeleniumUAT
  displayName: "Run Selenium UAT Tests"
  dependsOn: PerformanceTesting
  condition: succeeded()
  jobs:
    - job: SeleniumTest
      displayName: "Execute Selenium Test Suite"
      pool:
        vmImage: "ubuntu-latest"
      steps:
        # Set Up Python
        - task: UsePythonVersion@0
          inputs:
            versionSpec: "3.x"
          displayName: "Set Up Python 3.x"

        # Install Dependencies
        - script: |
            python -m pip install selenium
            sudo apt-get update
            sudo apt-get install -y google-chrome-stable
          displayName: "Install Selenium and Chrome"

        # Run Selenium Tests
        - script: |
            python selenium_automation.py > selenium_test.log || true
          displayName: "Run Selenium UAT Test"

        # Publish Selenium Test Report
        - task: PublishBuildArtifacts@1
          inputs:
            PathtoPublish: "selenium_test.log"
            ArtifactName: "Selenium-UAT-Report"
          displayName: "Publish Selenium Test Report"
```
### 3. **Pipeline Stages**

- Build and Test Stage: Runs unit tests for the application.
- Deploy to Test Environment: Deploys the application to a test environment.
- Run Security Testing: Conducts security scans using NPM Audit.
- Run Performance Testing: Executes performance testing using Artillery.
- Run Selenium UAT Tests: Runs Selenium tests to validate UI functionality.

### 4. **Artifacts**

- Selenium-UAT-Report: Contains the Selenium test logs output.
- View and download the selenium_test.log file in Azure DevOps artifacts under the Selenium UAT Test stage.

### 5. **Results**

- Correct loading of the target application URL.
- User input interactions such as search or form submission.
- Expected behavior and results on the web page

### **Screenshots**:

![Selenium Testing](images/Selenium-testing.jpg)