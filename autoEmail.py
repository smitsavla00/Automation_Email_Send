import smtplib
import pandas as pd
from email.message import EmailMessage

# Your email credentials
EMAIL_ADDRESS = " "  # Replace with your email
EMAIL_PASSWORD = " "  # Use an App Password (Recommended)
# Load job emails from CSV
contacts = pd.read_csv(r" ")  # Make sure this file exists (location of csv file)
# Email content
subject = " "  #Email Subject
body = """  


""" # Body of the email (content)

# Attachment
resume_path = r" "  # Make sure your attachment is in the same folder
# Send emails
for email in contacts["email"]:
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg.set_content(body)
    # Attach resume
    with open(resume_path, "rb") as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename="") #attachment name
    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
print("Emails Sent Successfully!")