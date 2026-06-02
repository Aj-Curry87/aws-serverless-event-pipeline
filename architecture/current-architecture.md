# AWS Serverless Event Pipeline - Current Architecture

This document represents the current AWS infrastructure created for the serverless event pipeline lab.

## Architecture Diagram

```mermaid
flowchart TD
    User[Client / curl / Postman] --> APIGW[API Gateway<br/>HTTP API<br/>POST /events]

    APIGW --> Producer[Producer Lambda<br/>event-producer-console]

    Producer --> Secrets[Secrets Manager<br/>event-pipeline/app-config<br/>appMode=training]

    Producer --> DynamoDB[DynamoDB<br/>EventTable<br/>PK: userId<br/>SK: timestamp]

    Producer --> Kinesis[Kinesis Data Stream<br/>event-stream<br/>Provisioned<br/>1 shard]

    Kinesis --> Consumer[Consumer Lambda<br/>event-consumer-console]

    Producer --> CWProducer[CloudWatch Logs<br/>Producer Lambda Logs]
    Consumer --> CWConsumer[CloudWatch Logs<br/>Consumer Lambda Logs]

    APIGW --> CWAPI[CloudWatch Metrics<br/>API Gateway Requests / Errors]
    DynamoDB --> CWDDB[CloudWatch Metrics<br/>DynamoDB Writes / Throttles]
    Kinesis --> CWKinesis[CloudWatch Metrics<br/>Kinesis Incoming Records / Iterator Age]

    IAM[IAM Roles and Policies] --> Producer
    IAM --> Consumer

    Budget[AWS Budgets<br/>Zero-spend + Monthly Cost Budget] -. cost guardrail .-> Kinesis
    Budget -. cost guardrail .-> DynamoDB
    Budget -. cost guardrail .-> Producer# AWS Serverless Event Pipeline - Current Architecture

This diagram represents the current AWS infrastructure created for the serverless event pipeline lab.

```mermaid
flowchart TD
    User[Client / curl / Postman] --> APIGW[API Gateway<br/>HTTP API<br/>POST /events]

    APIGW --> Producer[Producer Lambda<br/>event-producer-console]

    Producer --> Secrets[Secrets Manager<br/>event-pipeline/app-config<br/>appMode=training]

    Producer --> DynamoDB[DynamoDB<br/>EventTable<br/>PK: userId<br/>SK: timestamp]

    Producer --> Kinesis[Kinesis Data Stream<br/>event-stream<br/>Provisioned<br/>1 shard]

    Kinesis --> Consumer[Consumer Lambda<br/>event-consumer-console]

    Producer --> CWProducer[CloudWatch Logs<br/>Producer Lambda Logs]
    Consumer --> CWConsumer[CloudWatch Logs<br/>Consumer Lambda Logs]

    APIGW --> CWAPI[CloudWatch Metrics<br/>API Gateway Requests / Errors]
    DynamoDB --> CWDDB[CloudWatch Metrics<br/>DynamoDB Writes / Throttles]
    Kinesis --> CWKinesis[CloudWatch Metrics<br/>Kinesis Incoming Records / Iterator Age]

    IAM[IAM Roles and Policies] --> Producer
    IAM --> Consumer

    Budget[AWS Budgets<br/>Zero-spend + Monthly Cost Budget] -. cost guardrail .-> Kinesis
    Budget -. cost guardrail .-> DynamoDB
    Budget -. cost guardrail .-> Lambda
```

## Resource Inventory

| Resource | Name | Purpose |
|---|---|---|
| API Gateway | `event-pipeline-api` | Public HTTP API for `POST /events` |
| Producer Lambda | `event-producer-console` | Validates events, reads config, writes to DynamoDB, publishes to Kinesis |
| Consumer Lambda | `event-consumer-console` | Reads records from Kinesis and logs processed events |
| DynamoDB | `EventTable` | Stores validated event records |
| Kinesis Data Stream | `event-stream` | Streams events for asynchronous processing |
| Secrets Manager | `event-pipeline/app-config` | Stores application config value |
| CloudWatch Logs | `/aws/lambda/event-producer-console` | Producer Lambda logs |
| CloudWatch Logs | `/aws/lambda/event-consumer-console` | Consumer Lambda logs |
| IAM | Lambda execution roles | Least-privilege permissions for service access |
| AWS Budgets | Zero-spend and monthly budget | Cost-control guardrails |

## Event Flow

1. A client sends a `POST /events` request to API Gateway.
2. API Gateway invokes the producer Lambda.
3. Producer Lambda validates required fields: `userId`, `eventType`, and `source`.
4. Producer Lambda reads `appMode=training` from Secrets Manager.
5. Producer Lambda adds a timestamp and `appMode` to the event.
6. Producer Lambda saves the event to DynamoDB.
7. Producer Lambda publishes the event to Kinesis.
8. Kinesis triggers the consumer Lambda.
9. Consumer Lambda decodes the Kinesis record and logs the processed event to CloudWatch.

## Security Design

- Producer Lambda has scoped access to:
  - `dynamodb:PutItem` on `EventTable`
  - `kinesis:PutRecord` on `event-stream`
  - `secretsmanager:GetSecretValue` on `event-pipeline/app-config`
- Consumer Lambda has scoped read access to `event-stream`.
- No secrets are printed directly to CloudWatch logs.
- Public documentation uses placeholders for API ID and AWS account ID.

## Cost Controls

- AWS Budgets created before using Kinesis.
- Kinesis configured with provisioned capacity and 1 shard.
- No enhanced fan-out, Firehose, or Kinesis Data Analytics used.
- Kinesis should be deleted when not actively practicing.
