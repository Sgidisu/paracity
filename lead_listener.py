import os
import smtplib
import csv
from datetime import datetime
from flask import Flask, request, redirect
from flask_cors import CORS
from email.mime.text import MIMEText
from dotenv import load_dotenv # Run 'pip install python-dotenv' if not installed

# Load the secret password from the .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# --- EMAIL CONFIG ---
GMAIL_USER = "Sgidisu4life80@gmail.com"
# This pulls the password you just pasted into the .env file
GMAIL_PASSWORD = os.getenv("GMAIL_PASS") 
RECEIVER_EMAIL = "Sgidisu4life80@gmail.com"

def send_lead_alert(name, email, interest):
    msg = MIMEText(f"New Paracity Lead!\n\nName: {name}\nEmail: {email}\nInterest: {interest}")
    msg['Subject'] = f"🚨 New Lead: {name}"
    msg['From'] = GMAIL_USER
    msg['To'] = RECEIVER_EMAIL

    try:
        # Use port 465 for SSL (Standard for Gmail)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(GMAIL_USER, RECEIVER_EMAIL, msg.as_string())
        print("📧 Alert sent to inbox.")
    except Exception as e:
        print(f"❌ Email Error: {e}")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    interest = request.form.get('interest')
    
    # Save to CSV
    with open('lead_vault.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), name, email, interest])
    
    # Trigger Email
    send_lead_alert(name, email, interest)
    
    return redirect("https://sgidisu.github.io/paracity/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
