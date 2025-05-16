This README file gives the steps followed to complete the task. Apart from this, an additional documention is added to the repo to give more information on the poject.

API URL: https://s1atg1u0af.execute-api.eu-west-2.amazonaws.com (This is the created URL with the string)

### Setup & Installation

### 1. Prerequisites

- AWS account with access to IAM, Lambda, API Gateway
- AWS CLI installed and configured 
- Terraform CLI installed 
- Python installed

---

### 2. Clone the Project

- git clone https://github.com/Ashvini97/Arqiva_BE.git

### 3. Lambda function

- go to the project folder in the terminal and type below
- zip lambda.zip lambda_function.py

### 4. Deploy with terraform

- terraform init
- trraform apply (Type yes when prompted)

You will now get the publicly accessible url

Access the URL to get the string

### 5. Update the string without redeployment

- Option 1: AWS Console
  1. Go to Systems Manager > Parameter Store
  2. Click /html/dynamic_string
  3. Click Edit, change the value, and Save

- Option 2: AWS CLI

  In the terminal give te command below by changing the 'New value here'

  aws ssm put-parameter \
  --name /html/dynamic_string \
  --type String \
  --value "New value here" \
  --overwrite
