# gpt-lambda

This project demonstrates how to create and deploy a AWS Lambda function that uses OpenAI's GPT-3 model.

> **Note**<br />
> This code is currently set to run locally via `python3 lambda_function.py`, but by simply uncommenting the header and footer blocks and indenting the code, it will be ready to run a a lambda on AWS.

## Setup

### Prerequisites

Before you can set up the development environment for this project, you need to have the following tools installed:

- Python 3.8 or later
- pip 20.0 or later
- virtualenv 20.0 or later

### Setting up the environment

To set up the development environment for this project, follow these steps:

1. Create a new virtual environment for the project:

```
python -m venv .venvs/gpt-dev
```

2. Activate the virtual environment:

```
source .venvs/gpt-dev/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Use the gpt-dev virtual environment for running and developing the project's Python code.

To deactivate the virtual environment when you are finished working on the project, run the following command:

```
deactivate
```

With these steps, you will have a working development environment for the gpt-dev project that is isolated from other Python projects on your system. You can use this environment to develop and test the project's code without affecting other projects or your system's Python installation.

## Getting started

1. Create a new folder for the Lambda function:

```
mkdir gpt-lambda
cd gpt-lambda/
```

2. Create a new Python script for the Lambda function and proceed to update it as desired:

```
touch lambda_function.py
vim lambda_function.py
```

3. Install the required dependencies:

```
pip install --target ./package openai
```

4. Create the Lambda deployment package:

```
cd package/
zip -r ../gpt-lambda-package.zip .
cd ..
zip gpt-lambda-package.zip lambda_function.py
```

5. Deploy the Lambda function to AWS:

```
aws lambda create-function \
  --function-name gpt-lambda \
  --zip-file fileb://gpt-lambda-package.zip \
  --handler lambda_function.my_handler \
  --runtime python3.8 \
  --role arn:aws:iam::123456789012:role/my-lambda-role
```

## Making changes

To make changes to an already deployed Lambda function, edit the `lambda_function.py` file and then update the deployment package:

```
zip gpt-lambda-package.zip lambda_function.py
```

Then redeploy the updated package to AWS using the `aws lambda update-function-code` command.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
