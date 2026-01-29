import json
import os


def lambda_handler(event, context):
    """
    AWS Lambda handler function that returns a hello message.

    The message comes from the MSG environment variable.
    If MSG is not defined, it defaults to "world".

    Args:
        event: The event dict containing the request data
        context: The context object containing runtime information

    Returns:
        dict: Response with statusCode and body containing the hello message
    """
    # Get the message from environment variable, default to "world"
    msg = os.environ.get('MSG', 'world')

    # Create the response message
    response_message = f"hello {msg}"

    # Return the response in Lambda format
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': response_message
        })
    }
