import os
import smtplib
import csv
from datetime import datetime
from flask import Flask, request, redirect
from flask_cors import CORS
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load the secret password from the .env file
load_dotenv()

app = Flask(__name__)
# Security: Fixes the "Private Network" block in Chrome/Chromebook
CORS(app)

@app.after_request
def add_security_headers(response):
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response

# --- EMAIL CONFIG ---
GMAIL_USER = "Sgidisu4life80@gmail.com"
GMAIL_PASSWORD = os.getenv("GMAIL_PASS") 
RECEIVER_EMAIL = "Sgidisu4life80@gmail.com"

def send_lead_alert(name, email, interest):
    msg = MIMEText(f"New Paracity Lead!\n\nName: {name}\nEmail: {email}\nInterest: {interest}")
    msg['Subject'] = f"🚨 New Lead: {name}"
    msg['From'] = GMAIL_USER
    msg['To'] = RECEIVER_EMAIL

    try:
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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Save to CSV
    try:
        with open('lead_vault.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, name, email, interest])
    except Exception as e:
        print(f"❌ CSV Error: {e}")
    
    # 2. Trigger the Email Alert
    send_lead_alert(name, email, interest)
    
    # 3. Terminal Success Message
    print(f"\n\033[92m[SUCCESS]\033[0m Lead Captured: {name}")
    
    # 4. Redirect to the professional Thank You page
    return redirect("https://sgidisu.github.io/paracity/thank-you.html")

if __name__ == '__main__':
    # Running on 0.0.0.0 to ensure the Chromebook container bridge works
    app.run(host='0.0.0.0', port=5000)
