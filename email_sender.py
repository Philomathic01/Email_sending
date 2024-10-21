# email_sender.py

import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, message_body):
    from_address = "kishanyadavbhu001@gmail.com"  # Replace with your Gmail
    password = "uavm makp crhl fblh"  # Replace with your App Password

    # Create the email message
    msg = MIMEText(message_body)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(from_address, password)  # Login to your account
            server.sendmail(from_address, to_address, msg.as_string())
        return f"Email sent to {to_address} successfully."
    except Exception as e:
        return f"Failed to send email: {str(e)}"
