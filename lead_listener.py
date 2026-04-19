from flask import Flask, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    interest = request.form.get('interest')
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('lead_vault.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, name, email, interest])
        print(f"\n\033[92m[ALERT] NEW LEAD CAPTURED: {name} ({interest})\033[0m")
    
    # Redirect back to a 'thank you' or the original page
    return redirect("https://sgidisu.github.io/paracity/success.html")

if __name__ == '__main__':
    app.run(port=5000)
