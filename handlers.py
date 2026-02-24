import json
import requests
from config import ACCESS_TOKEN, WHATSAPP_API_URL

def send_message(recipient_id, message_text):
    """ Sends a message via WhatsApp Cloud API """
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "type": "text",
        "text": {"body": message_text}
    }

    response = requests.post(WHATSAPP_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return {"status": "success", "message": f"Sent to {recipient_id}"}
    else:
        return {"status": "error", "details": response.text}

def process_incoming_message(event, context):
    """ AWS Lambda function to process WhatsApp messages """
    data = json.loads(event["body"])  # Parse API Gateway payload

    if data and "entry" in data:
        for entry in data["entry"]:
            for change in entry.get("changes", []):
                if "messages" in change["value"]:
                    for message in change["value"]["messages"]:
                        sender_id = message.get("from", "0000000000")
                        message_text = message.get("text", {}).get("body", "Hello!")

                        print(f"Processing message from {sender_id}: {message_text}")

                        # Auto-response
                        response_text = f"Thanks for your message! You said: {message_text}"
                        send_message(sender_id, response_text)

    return {"statusCode": 200, "body": json.dumps({"status": "received"})}