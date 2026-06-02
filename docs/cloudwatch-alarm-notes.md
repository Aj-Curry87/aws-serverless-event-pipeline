# CloudWatch Alarm Notes

## Purpose

CloudWatch alarms notify the team when the event pipeline shows failure signals. Dashboards are useful when someone is watching, but alarms are useful when no one is watching.

## Alarms Created

| Alarm | Service | Metric | Meaning | First Response |
|---|---|---|---|---|
| ProducerLambdaErrors | Lambda | Errors | The API-facing Lambda failed. | Check producer Lambda logs. |
| ConsumerLambdaErrors | Lambda | Errors | The stream-processing Lambda failed. | Check consumer Lambda logs and Kinesis trigger. |
| KinesisWriteThroughputExceeded | Kinesis | WriteProvisionedThroughputExceeded | Kinesis write capacity was exceeded. | Check traffic volume, shard count, and producer retries. |

## Entry-Level Explanation

An alarm is a rule that watches a metric. A metric is a number AWS records, such as Lambda errors or Kinesis throttles. When the number crosses a threshold, CloudWatch changes the alarm state.

## Business Use Cases

### Finance
Alarms help detect payment, fraud, or transaction-processing failures quickly.

### Health
Alarms help teams respond when patient-related events, device alerts, or appointment workflows fail.

### Government
Alarms support incident response and operational accountability for audit or security event pipelines.

### Retail
Alarms help detect cart, checkout, order, and inventory event failures during normal traffic or sales spikes.

## Interview Explanation

I added CloudWatch alarms so the system does not rely only on manual log checking. The alarms watch Lambda errors and Kinesis throttling, which are early signs of failed event intake, failed processing, or stream pressure.
