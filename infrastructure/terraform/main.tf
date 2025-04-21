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

# Output the website URL
output "website_url" {
  value = aws_s3_bucket.frontend.website_endpoint
}