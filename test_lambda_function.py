import json
import pytest
from unittest.mock import patch
from lambda_function import lambda_handler


def test_lambda_handler_with_env_variable():
    """Test that lambda handler uses MSG environment variable when set."""
    with patch.dict('os.environ', {'MSG': 'Python'}):
        # Call the lambda handler
        result = lambda_handler({}, None)
        
        # Verify the response
        assert result['statusCode'] == 200
        body = json.loads(result['body'])
        assert body['message'] == 'hello Python'


def test_lambda_handler_without_env_variable():
    """Test that lambda handler defaults to 'world' when MSG is not set."""
    with patch.dict('os.environ', {}, clear=True):
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
        with patch.dict('os.environ', {'MSG': test_msg}):
            result = lambda_handler({}, None)
            
            assert result['statusCode'] == 200
            body = json.loads(result['body'])
            assert body['message'] == f'hello {test_msg}'


def test_lambda_handler_with_empty_string():
    """Test that lambda handler handles empty string in MSG."""
    with patch.dict('os.environ', {'MSG': ''}):
        result = lambda_handler({}, None)
        
        assert result['statusCode'] == 200
        body = json.loads(result['body'])
        assert body['message'] == 'hello '
