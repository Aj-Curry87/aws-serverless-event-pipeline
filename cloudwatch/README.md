# CloudWatch Dashboard

This folder contains the CloudWatch dashboard definition for the AWS Serverless Event Pipeline.

## Dashboard Name

`ServerlessEventPipelineDashboard`

## Dashboard Purpose

The dashboard provides operational visibility into:

- Producer Lambda invocations, errors, throttles, and duration
- Consumer Lambda invocations, errors, throttles, and duration
- DynamoDB write activity and throttling
- Kinesis incoming records, incoming bytes, and write throughput issues
- Kinesis consumer iterator age
- Recent producer Lambda logs
- Recent consumer Lambda logs

## Deploy Dashboard

```bash
aws cloudwatch put-dashboard \
  --dashboard-name ServerlessEventPipelineDashboard \
  --dashboard-body file://cloudwatch/serverless-event-pipeline-dashboard.json \
  --region us-east-2
