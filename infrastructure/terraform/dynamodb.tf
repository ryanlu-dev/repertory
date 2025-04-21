# DynamoDB Tables for Repertory Project
# Users Table
resource "aws_dynamodb_table" "users" {
  name         = "Repertory-Users"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"

  attribute {
    name = "userId"
    type = "S"
  }

  attribute {
    name = "email"
    type = "S"
  }

  global_secondary_index {
    name            = "email-index"
    hash_key        = "email"
    projection_type = "ALL"
  }

  tags = {
    Name        = "Repertory Users"
    Environment = "Dev"
    Project     = "Repertory"
  }
}

# Pieces Table
resource "aws_dynamodb_table" "pieces" {
  name         = "Repertory-Pieces"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "pieceId"

  attribute {
    name = "pieceId"
    type = "S"
  }

  attribute {
    name = "composer"
    type = "S"
  }

  attribute {
    name = "era"
    type = "S"
  }

  global_secondary_index {
    name            = "composer-index"
    hash_key        = "composer"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "era-index"
    hash_key        = "era"
    projection_type = "ALL"
  }

  tags = {
    Name        = "Repertory Pieces"
    Environment = "Dev"
    Project     = "Repertory"
  }
}

# UserRepertoire Table (junction table connecting users and pieces)
resource "aws_dynamodb_table" "user_repertoire" {
  name         = "Repertory-UserRepertoire"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "pieceId"

  attribute {
    name = "userId"
    type = "S"
  }

  attribute {
    name = "pieceId"
    type = "S"
  }

  global_secondary_index {
    name            = "pieceId-index"
    hash_key        = "pieceId"
    projection_type = "ALL"
  }

  tags = {
    Name        = "Repertory User Repertoire"
    Environment = "Dev"
    Project     = "Repertory"
  }
}

# Performances Table
resource "aws_dynamodb_table" "performances" {
  name         = "Repertory-Performances"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "performanceId"

  attribute {
    name = "userId"
    type = "S"
  }

  attribute {
    name = "performanceId"
    type = "S"
  }

  attribute {
    name = "performanceDate"
    type = "S"
  }

  global_secondary_index {
    name            = "date-index"
    hash_key        = "performanceDate"
    projection_type = "ALL"
  }

  tags = {
    Name        = "Repertory Performances"
    Environment = "Dev"
    Project     = "Repertory"
  }
}

# Achievements Table
resource "aws_dynamodb_table" "achievements" {
  name         = "Repertory-Achievements"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "achievementId"

  attribute {
    name = "achievementId"
    type = "S"
  }

  attribute {
    name = "achievementCategory"
    type = "S"
  }

  global_secondary_index {
    name            = "category-index"
    hash_key        = "achievementCategory"
    projection_type = "ALL"
  }

  tags = {
    Name        = "Repertory Achievements"
    Environment = "Dev"
    Project     = "Repertory"
  }
}

# UserAchievements Table (junction table connecting users and achievements)
resource "aws_dynamodb_table" "user_achievements" {
  name         = "Repertory-UserAchievements"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "achievementId"

  attribute {
    name = "userId"
    type = "S"
  }

  attribute {
    name = "achievementId"
    type = "S"
  }

  global_secondary_index {
    name            = "achievementId-index"
    hash_key        = "achievementId"
    projection_type = "ALL"
  }

  tags = {
    Name        = "Repertory User Achievements"
    Environment = "Dev"
    Project     = "Repertory"
  }
}

# Connections Table (for social features - following other musicians)
resource "aws_dynamodb_table" "connections" {
  name         = "Repertory-Connections"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "connectionId"

  attribute {
    name = "userId"
    type = "S"
  }

  attribute {
    name = "connectionId"
    type = "S"
  }

  global_secondary_index {
    name            = "connectionId-index"
    hash_key        = "connectionId"
    projection_type = "ALL"
  }

  tags = {
    Name        = "Repertory Connections"
    Environment = "Dev"
    Project     = "Repertory"
  }
}

# Output the table names for reference
output "users_table_name" {
  value = aws_dynamodb_table.users.name
}

output "pieces_table_name" {
  value = aws_dynamodb_table.pieces.name
}

output "user_repertoire_table_name" {
  value = aws_dynamodb_table.user_repertoire.name
}

output "performances_table_name" {
  value = aws_dynamodb_table.performances.name
}

output "achievements_table_name" {
  value = aws_dynamodb_table.achievements.name
}

output "user_achievements_table_name" {
  value = aws_dynamodb_table.user_achievements.name
}

output "connections_table_name" {
  value = aws_dynamodb_table.connections.name
}