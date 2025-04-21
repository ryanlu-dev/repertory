# Repertory

A platform for musicians to track performances, repertoire, and achievements.

## Development Status

Currently setting up initial infrastructure and basic components.

## Technologies Used

- Frontend: SvelteKit
- Backend: AWS Lambda, API Gateway, DynamoDB
- Infrastructure: Terraform
- Deployment: AWS S3, CloudFront

## Local Development

### Prerequisites
- AWS CLI
- Terraform
- Node.js
- Python 3.8+

### Frontend Development
1. Navigate to the frontend directory
2. Run `npm install`
3. Run `npm run dev`
4. Visit http://localhost:5173

### Deployment
1. Configure AWS credentials
2. Run `./scripts/deploy.sh`