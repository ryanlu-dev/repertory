#!/bin/bash

# Build the SvelteKit app
echo "Building SvelteKit app..."
cd ../frontend
npm run build

# Deploy to S3
echo "Deploying to S3..."
aws s3 sync build/ s3://repertory-frontend-ryanogen --delete

echo "Deployment complete!"
$SHELL