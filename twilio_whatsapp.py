import os
from twilio.rest import Client

def send_whatsapp_message(body, from_number,to_number):
    
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    
    if not account_sid or not auth_token:
        raise ValueError("Twilio credentials not found in environment variables")
    
    client = Client(account_sid, auth_token)
    from_number = '+' + ''.join(filter(str.isdigit, from_number))
    to_number = '+' + ''.join(filter(str.isdigit, to_number))
    
    try:
        client.messages.create(
            body=body,
            from_=from_number, 
            to=to_number
        )
        print(f"Message sent to {to_number}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    from_number = input("Enter the from number with country code (eg: +1234567890): ")
    to_number = input("Enter the number with country code (eg: +1234567890): ")
    message = input("Enter the message: ")
    send_whatsapp_message(message, from_number, to_number)   