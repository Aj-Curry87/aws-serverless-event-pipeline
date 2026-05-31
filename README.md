# AWS Serverless Event Pipeline

## Overview
This project is a beginner-friendly AWS serverless event pipeline. It shows how to receive events through an API, validate and process them with Lambda, store them in DynamoDB, stream them through Kinesis, and observe the system with CloudWatch and X-Ray.

## Project structure
- `architecture/` - diagrams or architecture notes
- `lambda/producer/` - producer Lambda code
- `lambda/consumer/` - consumer Lambda code
- `terraform/` - Infrastructure as Code for AWS resources
- `docs/` - troubleshooting, security, and cost notes
- `.github/workflows/` - CI workflows for Terraform

## Getting started
1. Install tools: AWS CLI, Terraform, Python 3.11, Git
2. Authenticate AWS CLI: `aws configure`
3. Build and test the Lambda code in the AWS Console
4. Add infrastructure with Terraform under `terraform/`

## Notes
- Use one AWS Region for all resources (for example `us-east-1`)
- Capture screenshots of working API calls, DynamoDB items, and CloudWatch logs
- Clean up resources when finished with `terraform destroy`
