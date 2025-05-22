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
        # Get current time
        now = datetime.datetime.now()
        
        # Add 1 minute to current time to ensure WhatsApp Web loads properly
        send_time = now + timedelta(minutes=1)
        
        # Remove any spaces or special characters from phone number
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        # Send message
        pywhatkit.sendwhatmsg(
            phone_no=f"+{phone_number}", 
            message=message,
            time_hour=send_time.hour,
            time_min=send_time.minute,
            wait_time=15,  # Wait 15 seconds for WhatsApp Web to load
            tab_close=True  # Close tab after sending message
        )
        print(f"Message scheduled to be sent to +{phone_number}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    phone_number = input("Enter phone number with country code (e.g., 1234567890): ")
    message = input("Enter your message: ")
    
    send_whatsapp_message(phone_number, message) 