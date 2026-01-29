# lambda-python

AWS Lambda function skeleton in Python that returns a hello message.

## Description

This Lambda function returns a greeting message in the format "hello {msg}", where the message comes from the `MSG` environment variable. If the environment variable is not defined, it defaults to "hello world".

## Lambda Function

The main Lambda handler is located in `lambda_function.py`. It implements the `lambda_handler` function which is the entry point for AWS Lambda.

### Function Signature

```python
def lambda_handler(event, context):
    """
    AWS Lambda handler function that returns a hello message.
    
    Args:
        event: The event dict containing the request data
        context: The context object containing runtime information
        
    Returns:
        dict: Response with statusCode and body containing the hello message
    """
```

### Environment Variables

- `MSG` (optional): The message to include in the greeting. If not set, defaults to "world".

### Response Format

The function returns a JSON response in the standard Lambda proxy integration format:

```json
{
    "statusCode": 200,
    "body": "{\"message\": \"hello world\"}"
}
```

## Examples

### With MSG environment variable set
```bash
# Set MSG=Python
# Response: {"message": "hello Python"}
```

### Without MSG environment variable
```bash
# MSG not set
# Response: {"message": "hello world"}
```

## Deployment to AWS Lambda

1. Package the lambda_function.py file
2. Create a Lambda function in AWS Console or using AWS CLI
3. Upload the lambda_function.py as the deployment package
4. Set the handler to `lambda_function.lambda_handler`
5. (Optional) Set the MSG environment variable in Lambda configuration
6. Deploy and test

### Using AWS CLI

```bash
# Create a deployment package
zip function.zip lambda_function.py

# Create the Lambda function
aws lambda create-function \
    --function-name hello-lambda \
    --runtime python3.9 \
    --role arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_LAMBDA_ROLE \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip \
    --environment Variables={MSG=AWS}
```

## Local Testing

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run Tests

```bash
pytest test_lambda_function.py -v
```

### Manual Testing

You can test the function locally by importing and calling it:

```python
from lambda_function import lambda_handler
import os

# Test with environment variable
os.environ['MSG'] = 'Python'
result = lambda_handler({}, None)
print(result)

# Test without environment variable
del os.environ['MSG']
result = lambda_handler({}, None)
print(result)
```

## Project Structure

```
lambda-python/
├── lambda_function.py       # Main Lambda handler
├── test_lambda_function.py  # Unit tests
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── .gitignore             # Git ignore patterns
```

## License

This project is provided as a skeleton/template for AWS Lambda functions.