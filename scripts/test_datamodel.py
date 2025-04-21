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
pieces_table = dynamodb.Table('Repertory-Pieces')
repertoire_table = dynamodb.Table('Repertory-UserRepertoire')
performances_table = dynamodb.Table('Repertory-Performances')
achievements_table = dynamodb.Table('Repertory-Achievements')
user_achievements_table = dynamodb.Table('Repertory-UserAchievements')

# Helper function to pretty print DynamoDB items
def pretty_print(title, items):
    print(f"\n{title}:")
    print(json.dumps(items, indent=2, cls=DynamoDBEncoder))

# Function to get a piece by ID
def get_piece(piece_id):
    response = pieces_table.get_item(
        Key={'pieceId': piece_id}
    )
    return response.get('Item')

# Function to get pieces by era
def get_pieces_by_era(era):
    response = pieces_table.query(
        IndexName='era-index',
        KeyConditionExpression=Key('era').eq(era)
    )
    return response['Items']

# Function to get user performances
def get_user_performances(user_id):
    response = performances_table.query(
        KeyConditionExpression=Key('userId').eq(user_id)
    )
    return response['Items']

# Function to get all performances for a specific date
def get_performances_by_date(date):
    response = performances_table.query(
        IndexName='date-index',
        KeyConditionExpression=Key('performanceDate').eq(date)
    )
    return response['Items']

# Function to get an achievement by ID
def get_achievement(achievement_id):
    response = achievements_table.get_item(
        Key={'achievementId': achievement_id}
    )
    return response.get('Item')

# Function to get all achievements in a category
def get_achievements_by_category(category):
    response = achievements_table.query(
        IndexName='category-index',
        KeyConditionExpression=Key('achievementCategory').eq(category)
    )
    return response['Items']

# Function to get user achievements
def get_user_achievements(user_id):
    response = user_achievements_table.query(
        KeyConditionExpression=Key('userId').eq(user_id)
    )
    return response['Items']

# Function to get all users who earned a specific achievement
def get_users_with_achievement(achievement_id):
    response = user_achievements_table.query(
        IndexName='achievementId-index',
        KeyConditionExpression=Key('achievementId').eq(achievement_id)
    )
    return response['Items']

# Function to get a user's full profile with repertoire, performances, and achievements
def get_user_profile(user_id):
    # Get basic user info
    user_response = users_table.get_item(
        Key={'userId': user_id}
    )
    user = user_response.get('Item')
    
    if not user:
        return None
    
    # Get repertoire
    repertoire_response = repertoire_table.query(
        KeyConditionExpression=Key('userId').eq(user_id)
    )
    repertoire = repertoire_response['Items']
    
    # Get performances
    performances_response = performances_table.query(
        KeyConditionExpression=Key('userId').eq(user_id)
    )
    performances = performances_response['Items']
    
    # Get achievements
    achievements_response = user_achievements_table.query(
        KeyConditionExpression=Key('userId').eq(user_id)
    )
    user_achievements = achievements_response['Items']
    
    # Enrich user achievements with details
    enriched_achievements = []
    for ua in user_achievements:
        achievement = get_achievement(ua['achievementId'])
        if achievement:
            enriched_achievements.append({
                'achievementDetails': achievement,
                'earnedAt': ua.get('earnedAt'),
                'progress': ua.get('progress')
            })
    
    # Build complete profile
    profile = {
        'userInfo': user,
        'repertoire': repertoire,
        'performances': performances,
        'achievements': enriched_achievements
    }
    
    return profile

# Test our functions
if __name__ == "__main__":
    # Get all baroque pieces
    baroque_pieces = get_pieces_by_era('Baroque')
    pretty_print("Baroque pieces", baroque_pieces)
    
    # Get John's performances
    john_performances = get_user_performances('user123')
    pretty_print("John's performances", john_performances)
    
    # Get performances on March 15, 2025
    march_performances = get_performances_by_date('2025-03-15')
    pretty_print("Performances on March 15, 2025", march_performances)
    
    # Get Performance category achievements
    performance_achievements = get_achievements_by_category('Performance')
    pretty_print("Performance achievements", performance_achievements)
    
    # Get users who earned the "First Performance" achievement
    users_with_first_performance = get_users_with_achievement('ach1')
    pretty_print("Users with 'First Performance' achievement", users_with_first_performance)
    
    # Get John's complete profile
    john_profile = get_user_profile('user123')
    pretty_print("John's complete profile", john_profile)