# WhatsApp Message Sender

This is a simple Python script that allows you to send WhatsApp messages programmatically using the `pywhatkit` library.

## Prerequisites

- Python 3.6 or higher
- WhatsApp Web access
- A web browser (Chrome recommended)

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python send_whatsapp.py
```

2. When prompted:
   - Specify if sending a message to an individual or group
   - If sending to a an individual
       - Enter the recipient's phone number with country code
       - Enter the message you want to send
   - If sending to a group
       - Enter the rgroup id
       - Enter the message you want to send


The script will:
1. Open WhatsApp Web in your default browser
2. Wait for it to load
3. Send the message automatically
4. Close the browser tab

## Important Notes

- Make sure you're logged into WhatsApp Web before running the script
- The phone number should include the country code without any special characters
- Keep the WhatsApp Web tab active until the message is sent

## Error Handling

If any error occurs during the process, the script will display an error message explaining what went wrong.