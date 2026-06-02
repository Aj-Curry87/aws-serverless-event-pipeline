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
# CloudWatch Alarm Notes

## Purpose

CloudWatch alarms monitor important failure signals in the serverless event pipeline. Dashboards help when an engineer is actively looking. Alarms help when no one is actively watching the system.

## Current Alarms

| Alarm | Service | Metric | Threshold | What It Means | First Troubleshooting Step |
|---|---|---|---|---|---|
| ProducerLambdaErrors | Lambda | Errors | >= 1 error in 5 minutes | The API-facing Lambda failed while handling an event. | Check `/aws/lambda/event-producer-console` logs. |
| ConsumerLambdaErrors | Lambda | Errors | >= 1 error in 5 minutes | The Kinesis consumer Lambda failed while processing stream records. | Check `/aws/lambda/event-consumer-console` logs and Kinesis trigger status. |
| KinesisWriteThroughputExceeded | Kinesis | WriteProvisionedThroughputExceeded | >= 1 throttle in 5 minutes | Kinesis received more write traffic than the stream could handle. | Check producer traffic volume, shard count, and retry behavior. |

## Entry-Level Explanation

A CloudWatch alarm watches a metric. A metric is a number AWS records, such as Lambda errors or Kinesis throttles.

If the metric crosses a limit, CloudWatch changes the alarm state.

Example:

If the Producer Lambda has one or more errors within five minutes, the `ProducerLambdaErrors` alarm changes state.

## Day 4 Test Result

A test event was sent through API Gateway.

Sanitized test command:

```bash
curl -X POST "https://YOUR_API_ID.execute-api.us-east-2.amazonaws.com/events" \
  -H "Content-Type: application/json" \
  -d '{"userId":"your-ID","eventType":"alarm-test","source":"day-4-cloudwatch-alarms"}'
