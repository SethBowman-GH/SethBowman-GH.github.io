from handlers import process_incoming_message

def lambda_handler(event, context):
    return process_incoming_message(event, context)