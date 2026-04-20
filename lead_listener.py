import csv
from datetime import datetime

def log_lead(name, email, interest):
    """Logs a new investor lead to the Paracity Vault."""
    try:
        with open('lead_vault.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), name, email, interest, "PENDING"])
        return True
    except Exception as e:
        print(f"Error logging lead: {e}")
        return False
