import smtplib

# Replace with your email and password
email = 'pugalendhis59@gmail.com'
password = 'Betta@124'

# Replace with the recipient's email
recipient_email = 'pugazhendhi235@gmail.com'

message = f"Subject: Test Email\n\nThis is a test message."

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Create a secure connection with the Gmail SMTP server (SSL/TLS)
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls()

    # Login using your email and password
    server.login(email, password)

    # Send the message
    server.sendmail(email, recipient_email, message)