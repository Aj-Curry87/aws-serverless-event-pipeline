import json
import os
from datetime import datetime, timezone

import boto3

REQUIRED_FIELDS = ["userId", "eventType", "source"]

EVENT_TABLE = os.environ.get("EVENT_TABLE", "EventTable")
EVENT_STREAM = os.environ.get("EVENT_STREAM", "event-stream")

dynamodb = boto3.resource("dynamodb")
kinesis = boto3.client("kinesis")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }


def lambda_handler(event, context):
    try:
        print("Received event from caller")

        body = event.get("body", event)

        if isinstance(body, str):
            body = json.loads(body)

        missing = [field for field in REQUIRED_FIELDS if field not in body]

        if missing:
            print(f"Validation failed. Missing fields: {missing}")
            return response(400, {
                "message": "Missing required fields",
                "missing": missing
            })

        body.setdefault("timestamp", datetime.now(timezone.utc).isoformat())

        print(
            f"Validated event: userId={body.get('userId')}, "
            f"eventType={body.get('eventType')}, "
            f"source={body.get('source')}"
        )

        table = dynamodb.Table(EVENT_TABLE)
        table.put_item(Item=body)

        print(f"Saved event to DynamoDB table: {EVENT_TABLE}")

        kinesis_response = kinesis.put_record(
            StreamName=EVENT_STREAM,
            Data=json.dumps(body).encode("utf-8"),
            PartitionKey=body["userId"]
        )

        print(
            f"Published event to Kinesis stream: {EVENT_STREAM}, "
            f"shardId={kinesis_response.get('ShardId')}, "
            f"sequenceNumber={kinesis_response.get('SequenceNumber')}"
        )

        return response(200, {
            "message": "Event accepted, saved to DynamoDB, and published to Kinesis",
            "event": body
        })

    except Exception as exc:
        print(f"Unhandled error: {str(exc)}")
        return response(500, {
            "message": "Unhandled error",
            "error": str(exc)
        })
