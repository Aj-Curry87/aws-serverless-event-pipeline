# AWS Serverless Event Pipeline

## Overview

This project is a beginner-friendly, production-inspired AWS serverless event pipeline built for hands-on AWS Infrastructure Engineer practice.

The pipeline receives events through API Gateway, validates and processes them with Lambda, stores them in DynamoDB, streams them through Kinesis, and uses CloudWatch for logs and operational visibility.

## Architecture

```text
API Gateway POST /events
→ Producer Lambda
→ Secrets Manager
→ DynamoDB EventTable
→ Kinesis event-stream
→ Consumer Lambda
→ CloudWatch Logs
