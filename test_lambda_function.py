import os
import json
import pytest
from lambda_function import lambda_handler


def test_lambda_handler_with_env_variable():
    """Test that lambda handler uses MSG environment variable when set."""
    # Set the MSG environment variable
    os.environ['MSG'] = 'Python'
    
    # Call the lambda handler
    result = lambda_handler({}, None)
    
    # Verify the response
    assert result['statusCode'] == 200
    body = json.loads(result['body'])
    assert body['message'] == 'hello Python'
    
    # Clean up
    del os.environ['MSG']


def test_lambda_handler_without_env_variable():
    """Test that lambda handler defaults to 'world' when MSG is not set."""
    # Ensure MSG is not set
    if 'MSG' in os.environ:
        del os.environ['MSG']
    
    # Call the lambda handler
    result = lambda_handler({}, None)
    
    # Verify the response
    assert result['statusCode'] == 200
    body = json.loads(result['body'])
    assert body['message'] == 'hello world'


def test_lambda_handler_with_custom_message():
    """Test that lambda handler works with various custom messages."""
    test_messages = ['AWS', 'Lambda', 'Testing', 'CI/CD']
    
    for test_msg in test_messages:
        os.environ['MSG'] = test_msg
        result = lambda_handler({}, None)
        
        assert result['statusCode'] == 200
        body = json.loads(result['body'])
        assert body['message'] == f'hello {test_msg}'
    
    # Clean up
    if 'MSG' in os.environ:
        del os.environ['MSG']


def test_lambda_handler_with_empty_string():
    """Test that lambda handler handles empty string in MSG."""
    os.environ['MSG'] = ''
    
    result = lambda_handler({}, None)
    
    assert result['statusCode'] == 200
    body = json.loads(result['body'])
    assert body['message'] == 'hello '
    
    # Clean up
    del os.environ['MSG']
