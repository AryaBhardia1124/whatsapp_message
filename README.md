# WhatsApp Message Sender

A Python script that provides two methods to send WhatsApp messages:
1. Using PyWhatKit (via WhatsApp Web)
2. Using Twilio API (professional/business usage)

## Prerequisites

- Python 3.9 or higher
- For PyWhatKit: WhatsApp Web access and a web browser (Chrome recommended)
- For Twilio: A Twilio account with WhatsApp capabilities
- Virtual environment (recommended)

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd whatsapp_message
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Method 1: Using PyWhatKit (WhatsApp Web)

### Setup
- Make sure you're logged into WhatsApp Web before running the script
- No additional credentials needed

### Usage
Run the script:
```bash
python send_whatsapp.py
```

The script will:
1. Open WhatsApp Web in your default browser
2. Prompt for recipient's phone number and message
3. Send the message automatically
4. Close the browser tab

### Notes
- Keep the WhatsApp Web tab active until the message is sent
- Phone numbers should include country code (e.g., "1234567890" for +1 234567890)
- Free to use, but requires manual WhatsApp Web login

## Method 2: Using Twilio API

### Setup
1. Sign up for a [Twilio account](https://www.twilio.com/try-twilio)
2. Get your Account SID and Auth Token from the Twilio Console
3. Enable WhatsApp in your Twilio account
4. Create a `.env` file in the project root:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

### Usage
Run the script:
```bash
python twilio_whatsapp.py
```

The script will prompt you for:
- Sender's WhatsApp number (with country code)
- Recipient's WhatsApp number (with country code)
- Message content

### Notes
- Requires Twilio account and credits
- More reliable for business usage
- No browser interaction needed

## Features

### PyWhatKit Method
- Browser-based automation
- No API costs
- Requires active browser session

### Twilio Method
- Professional API integration
- Automatic phone number formatting
- Error handling and user feedback
- Environment variable support
- No browser dependency

## Dependencies

- pywhatkit==5.4 (for WhatsApp Web method)
- twilio==8.12.0 (for Twilio API method)
- python-dotenv==1.0.0 (for environment variables)

## License

This project is licensed under the MIT License - see the LICENSE file for details.