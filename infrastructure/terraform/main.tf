provider "aws" {
  region = "us-east-2" 
}

# S3 bucket for frontend hosting
resource "aws_s3_bucket" "frontend" {
  bucket = "repertory-frontend-ryanogen"
  
  tags = {
    Name        = "Repertory Frontend"
    Environment = "Dev"
  }
}

# S3 bucket policy to allow public read access
resource "aws_s3_bucket_policy" "frontend_policy" {
  bucket = aws_s3_bucket.frontend.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = ["s3:GetObject"]
        Effect    = "Allow"
        Resource  = "${aws_s3_bucket.frontend.arn}/*"
        Principal = "*"
      },
    ]
  })
}

# Enable website hosting on the S3 bucket
resource "aws_s3_bucket_website_configuration" "frontend_website" {
  bucket = aws_s3_bucket.frontend.id
  
  index_document {
    suffix = "index.html"
  }
  
  error_document {
    key = "index.html"  # SPA fallback
  }
}

# Output the website URL
output "website_url" {
  value = aws_s3_bucket_website_configuration.frontend_website.website_endpoint
}

# IAM role for Lambda
resource "aws_iam_role" "lambda_exec" {
  name = "repertory_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Lambda function
resource "aws_lambda_function" "hello_world" {
  function_name = "repertory-hello-world"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "index.lambda_handler"
  runtime       = "python3.11"
  
  filename      = "../../backend/lambda/hello-world.zip"
  
  environment {
    variables = {
      ENV = "dev"
    }
  }
}