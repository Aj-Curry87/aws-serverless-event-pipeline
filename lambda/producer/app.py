import json
import os
from datetime import datetime, timezone

import boto3

REQUIRED_FIELDS = ["userId", "eventType", "source"]

EVENT_TABLE = os.environ.get("EVENT_TABLE", "EventTable")
dynamodb = boto3.resource("dynamodb")


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

        return response(200, {
            "message": "Event accepted and saved to DynamoDB",
            "event": body
        })

    except Exception as exc:
        print(f"Unhandled error: {str(exc)}")
        return response(500, {
            "message": "Unhandled error",
            "error": str(exc)
        })
