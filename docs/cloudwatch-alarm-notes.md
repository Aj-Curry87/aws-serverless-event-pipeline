## Troubleshooting Finding

During alarm testing, the API returned an unhandled error because the Producer Lambda attempted to write to a Kinesis stream named `event-stream`, but the stream was not found in `us-east-2`.

Root cause possibilities:
- Kinesis stream was not created.
- Stream name did not match the Lambda configuration.
- Stream existed in a different Region.
- Lambda environment variable or hardcoded stream name was incorrect.

Resolution:
- Verified Kinesis streams with `aws kinesis list-streams --region us-east-2`.
- Created or corrected the stream name as needed.
- Retested the API after confirming the stream was active.

Entry-level explanation:
The API worked, but the backend Lambda could not place the event onto the Kinesis stream because the expected stream was missing.
## Day 4 Test Finding

While testing the CloudWatch alarms, the API returned an error because the Producer Lambda attempted to write to the Kinesis stream before the expected stream was available. 

Creation Command:

aws kinesis create-stream \
  --stream-name YOUR-STREAM NAME \
  --shard-count YOUR SHARD COUNT \
  --region Your Region

Validation command:

```bash
aws kinesis list-streams --region Your Region
