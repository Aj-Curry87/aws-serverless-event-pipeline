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
```

## Test Dashboard

```bash
curl -X POST "https://YOUR_API_ID.execute-api.us-east-2.amazonaws.com/events" \
  -H "Content-Type: application/json" \
  -d '{"userId":"aj-001","eventType":"dashboard-test","source":"cloudwatch-dashboard"}'
```

Then refresh the CloudWatch dashboard and verify activity in:

- Producer Lambda metrics
- Consumer Lambda metrics
- DynamoDB write metrics
- Kinesis incoming records
- Producer logs
- Consumer logs

## Interview Explanation

This dashboard shows that I can monitor and operate the infrastructure I build. It gives visibility into Lambda health, DynamoDB writes, Kinesis stream activity, consumer processing, iterator age, and recent logs.

This moves the project beyond simply deploying AWS services and demonstrates operational support thinking.
