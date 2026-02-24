import boto3
import json

# AWS Secrets Manager integration
def get_secret(secret_name):
    """Fetch secret from AWS Secrets Manager"""
    client = boto3.client("secretsmanager", region_name="us-east-1")  # Change region if needed
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

# Load secrets from AWS Secrets Manager
secrets = get_secret("whatsapp_chatbot_secrets")

VERIFY_TOKEN = secrets.get("VERIFY_TOKEN", "default_verify_token")
ACCESS_TOKEN = secrets.get("ACCESS_TOKEN", "default_access_token")

# WhatsApp API URL (Replace with your own business phone ID)
WHATSAPP_API_URL = "https://graph.facebook.com/v18.0/1234567890/messages"