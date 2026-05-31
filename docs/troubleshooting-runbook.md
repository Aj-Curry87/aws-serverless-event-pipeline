# Troubleshooting Runbook

## Day 2 - API Gateway to Lambda Test

### Successful API Request
Command:
curl -X POST "https://069xyjjc2f.execute-api.us-east-2.amazonaws.com/events" \
  -H "Content-Type: application/json" \
  -d '{"userId":"aj-001","eventType":"login","source":"curl"}'

Result:
The API returned "Event accepted by Lambda" with userId, eventType, source, and timestamp.

Lesson:
API Gateway successfully routed POST /events to the producer Lambda.

### Validation Failure Test
Command:
curl -X POST "https://069xyjjc2f.execute-api.us-east-2.amazonaws.com/events" \
  -H "Content-Type: application/json" \
  -d '{"userId":"aj-001","source":"curl"}'

Expected Result:
The Lambda should return statusCode 400 and report that eventType is missing.

Lesson:
The Lambda validates input and returns controlled errors instead of failing silently.
