# X-Ray Notes

## Day 5 Trace Validation

X-Ray tracing was enabled for the serverless event pipeline.

The CloudWatch Trace Map showed the `event-producer-console` Lambda function receiving traced requests.

Observed signals:
- Producer Lambda appeared in the trace map.
- Request count was visible.
- Latency was visible.
- Fault rate showed 0.00/min during the validation window.

## Explanation

CloudWatch Logs show what a function printed or what error occurred.

X-Ray shows the path of a request and how long parts of the system took.

Logs are useful for reading details. Traces are useful for understanding request flow and latency.

## Business Use Cases

### Finance
X-Ray can help identify latency in transaction validation, payment processing, or fraud event pipelines.

### Healthcare
X-Ray can help troubleshoot delays in patient alert, appointment, or device telemetry workflows.

### Government
X-Ray supports traceability for audit, security, and operational event processing systems.

### Retail
X-Ray can help identify slow points in checkout, order, cart, or inventory event workflows.

## Interview Explanation

I enabled X-Ray tracing so I could move beyond logs and understand request latency and service flow. After sending a test event, I verified that the Producer Lambda appeared in the CloudWatch Trace Map with request count, latency, and fault metrics.


# X-Ray Notes

## Purpose

AWS X-Ray helps trace requests through the serverless event pipeline.

CloudWatch Logs show what happened inside a function.

CloudWatch Metrics show numbers such as invocations, errors, duration, and throttles.

CloudWatch Alarms notify the team when metrics cross a threshold.

X-Ray helps show the path of a request and where latency occurs.

## Services Traced

| Service | Tracing Purpose |
|---|---|
| Producer Lambda | Shows request latency for the API-facing Lambda. |
| Consumer Lambda | Shows processing behavior for records consumed from Kinesis. |

## Day 5 Validation

X-Ray tracing was enabled for the producer and consumer Lambda functions.

Validation commands:

```bash
aws lambda get-function-configuration \
  --function-name event-producer-console \
  --region us-east-2 \
  --query "TracingConfig"

aws lambda get-function-configuration \
  --function-name event-consumer-console \
  --region us-east-2 \
  --query "TracingConfig"
