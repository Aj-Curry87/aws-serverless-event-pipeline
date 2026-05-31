import json
import os
from datetime import datetime, timezone

REQUIRED_FIELDS = ["userId", "eventType", "source"]


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }


def lambda_handler(event, context):
    try:
        body = event.get("body", event)
        if isinstance(body, str):
            body = json.loads(body)

        missing = [field for field in REQUIRED_FIELDS if field not in body]
        if missing:
            return response(400, {"message": "Missing required fields", "missing": missing})

        body.setdefault("timestamp", datetime.now(timezone.utc).isoformat())

        return response(200, {
            "message": "Event accepted by Lambda",
            "event": body
        })
    except Exception as exc:
        return response(500, {"message": "Unhandled error", "error": str(exc)})
