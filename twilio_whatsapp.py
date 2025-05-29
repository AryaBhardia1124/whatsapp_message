import os
from twilio.rest import Client

account_sid = ''
auth_token = '[]'
client = Client(account_sid, auth_token)

def send_whatsapp_message(body, to_number):

    from_number = 'whatsapp:+'
    to_number = 'whatsapp:+' + ''.join(filter(str.isdigit, to_number))
    try:
        client.messages.create(body = body,
                               from_ = from_number, 
                               to = to_number)
        print(f"Message sent to {to_number}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    to_number = input("Enter the  number with country code (eg: +1234567890): ")
    message = input("Enter the message: ")
    send_whatsapp_message(message, to_number)   