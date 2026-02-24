from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook verification token (replace with your actual token)
VERIFY_TOKEN = "1234567890"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verification for WhatsApp API
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    elif request.method == 'POST':
        # Handle incoming messages
        data = request.get_json()
        print("Received:", data)  # Log the incoming request
        
        # Basic response logic (modify as needed)
        if data and "entry" in data:
            for entry in data["entry"]:
                for change in entry.get("changes", []):
                    if "messages" in change["value"]:
                        for message in change["value"]["messages"]:
                            sender_id = message.get("from", "0000000000")  # Fake number
                            message_text = message.get("text", {}).get("body", "Hello!")

                            print(f"Message from {sender_id}: {message_text}")

                            # Here you could call a function to send a response message

        return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)