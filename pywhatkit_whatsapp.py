import pywhatkit
import datetime
from datetime import timedelta
import os
from dotenv import load_dotenv

def send_whatsapp_message_individual(phone_number, message):
    try:
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        pywhatkit.sendwhatmsg_instantly(
            phone_no = phone_number, 
            message = message, 
            tab_close = True  
        )
        print(f"Message being sent to +{phone_number}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def send_whatsapp_message_group(group_id, message):
    try:    
        pywhatkit.sendwhatmsg_to_group_instantly(
            group_id = group_id, 
            message = message, 
            tab_close = True
        )
        print(f"Message being sent to {group_id}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    variable = input("Are you sending a message to an individual or a group? (I/G): ")
    if variable == "I" or variable == "i":
        phone_number = '+' + str(input("Enter phone number with country code (e.g., 1234567890): "))
        message = input("Enter your message: ")
        send_whatsapp_message_individual(phone_number, message) 
    elif variable == "G" or variable == "g":
        group_id = str(input("Enter group ID: "))
        message = input("Enter your message: ")
        send_whatsapp_message_group(group_id, message) 
    else:
        print("Invalid input. Please enter 'I' for individual or 'G' for group.")

    
    