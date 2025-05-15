📧 Automated Bulk Email Sender Using Python
This project is a Python script that allows you to automatically send personalized emails in bulk using data from a .csv file. It supports attachments (like your resume) and is ideal for job applications or any form of mass email outreach.

🚀 Features
Read recipient emails from a CSV file
Send emails securely using Gmail (SMTP with SSL)
Attach PDF documents like resumes
Loop through each contact and send an individual email
Fully customizable subject and body content

🧾 Requirements
Make sure you have the following installed:
pip install pandas
Python version: 3.6+

🔐 Gmail SMTP Setup
Enable 2-Step Verification on your Gmail account.

Generate an App Password:
Go to Google Account Security
Click "App Passwords"
Select Mail and Your Device, then generate
Use the 16-character password in place of your Gmail password

📂 File Structure
.
├── send_email.py          # Main script
├── contacts.csv           # List of email addresses
├── resume.pdf             # File to be attached
└── README.md              # Project instructions
📝 CSV Format (contacts.csv)
This file should include a column named email. Example:
email
john.doe@example.com
jane.smith@example.com
...

⚙️ Configuration (Before You Run)
In send_email.py, update the following:

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
contacts = pd.read_csv(r"contacts.csv")
subject = "Your Email Subject"
body = """
Write your email content here.
Best regards,
Your Name
"""
resume_path = r"resume.pdf"

Make sure:
The CSV file and the attachment are in the same directory or provide the full path.
The filename="" in the attachment section is optionally filled with something like "resume.pdf" for clarity.

▶️ How to Run
python send_email.py
Once executed, it will send emails to all addresses listed in the CSV with the provided content and attachment.

⚠️ Notes
Use this script responsibly. Don't spam.
Ensure you're complying with email sending policies (especially if using Gmail).
Gmail has limits on the number of emails you can send per day.

📌 To-Do / Improvements (Optional)
Add email templating with placeholders (e.g., "Hi {name}")
Add HTML email support
Add logging (success/failure)
Error handling for invalid email formats or SMTP failures

📬 Contact
For issues or questions, feel free to open an issue on GitHub or reach out.
