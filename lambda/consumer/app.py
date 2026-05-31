import base64
import json


def lambda_handler(event, context):
    processed = 0

    print(f"Received batch from Kinesis with {len(event.get('Records', []))} records")

    for record in event.get("Records", []):
        payload = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        data = json.loads(payload)

        print(
            f"Processed event: userId={data.get('userId')}, "
            f"eventType={data.get('eventType')}, "
            f"source={data.get('source')}, "
            f"timestamp={data.get('timestamp')}"
        )

        processed += 1

    return {
        "processed": processed
    }
