import pywhatkit
import datetime
from datetime import timedelta
import os
from dotenv import load_dotenv

def send_whatsapp_message(phone_number, message):
    """
    Send a WhatsApp message to a specified phone number.
    
    Args:
        phone_number (str): Phone number with country code (e.g., '+1234567890')
        message (str): Message to be sent
    """
    try:
        # Remove any spaces or special characters from phone number
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        # Send message instantly
        pywhatkit.sendwhatmsg_instantly(
            phone_no=f"+{phone_number}", 
            message=message,
            wait_time=10,  # Wait 10 seconds for WhatsApp Web to load
            tab_close=True  # Close tab after sending message
        )
        print(f"Message being sent to +{phone_number}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    phone_number = input("Enter phone number with country code (e.g., 1234567890): ")
    message = input("Enter your message: ")
    
    send_whatsapp_message(phone_number, message) 