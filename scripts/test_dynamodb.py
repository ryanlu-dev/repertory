import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal

# Custom JSON encoder for DynamoDB types
class DynamoDBEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, Decimal):
            if obj % 1 == 0:
                return int(obj)
            else:
                return float(obj)
        return json.JSONEncoder.default(self, obj)

# Connect to local DynamoDB
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Get table references
users_table = dynamodb.Table('Repertory-Users')
repertoire_table = dynamodb.Table('Repertory-UserRepertoire')

# Function to get a user's repertoire
def get_user_repertoire(user_id):
    response = repertoire_table.query(
        KeyConditionExpression=Key('userId').eq(user_id)
    )
    return response['Items']

# Function to get users by instrument
def get_users_by_instrument(instrument):
    response = users_table.scan(
        FilterExpression=Attr('instruments').contains(instrument)
    )
    return response['Items']

# Function to add a new piece to a user's repertoire
def add_to_repertoire(user_id, piece_id, title, composer, piece_status="learning"):
    response = repertoire_table.put_item(
        Item={
            'userId': user_id,
            'pieceId': piece_id,
            'title': title,
            'composer': composer,
            'pieceStatus': piece_status
        }
    )
    return response

# Function to find all pieces with a specific status
def find_pieces_by_status(user_id, status_value):
    response = repertoire_table.query(
        KeyConditionExpression=Key('userId').eq(user_id),
        FilterExpression=Attr('pieceStatus').eq(status_value)
    )
    return response['Items']

# Helper function to pretty print DynamoDB items
def pretty_print(title, items):
    print(f"\n{title}:")
    print(json.dumps(items, indent=2, cls=DynamoDBEncoder))

# Test our functions
if __name__ == "__main__":
    # Get John's repertoire
    john_repertoire = get_user_repertoire('user123')
    pretty_print("John's repertoire", john_repertoire)
    
    # Find all violinists
    violinists = get_users_by_instrument('Violin')
    pretty_print("Violinists", violinists)
    
    # Add a new piece to Jane's repertoire
    add_to_repertoire('user456', 'piece4', 'Cello Concerto', 'Dvorak', 'learning')
    
    # Check Jane's updated repertoire
    jane_repertoire = get_user_repertoire('user456')
    pretty_print("Jane's updated repertoire", jane_repertoire)
    
    # Find all of John's mastered pieces
    mastered_pieces = find_pieces_by_status('user123', 'mastered')
    pretty_print("John's mastered pieces", mastered_pieces)