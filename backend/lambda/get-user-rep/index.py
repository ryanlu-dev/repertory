import boto3
from boto3.dynamodb.conditions import Key

# Get references to your DynamoDB tables
dynamodb = boto3.resource('dynamodb')
user_repertoire_table = dynamodb.Table('Repertory-UserRepertoire')

def get_user_repertoire(user_id):
    """
    Retrieve all pieces in a user's repertoire
    """
    # Query the table using the partition key (userId)
    response = user_repertoire_table.query(
        KeyConditionExpression=Key('userId').eq(user_id)
    )
    
    # Return the items (pieces in the user's repertoire)
    return response['Items']