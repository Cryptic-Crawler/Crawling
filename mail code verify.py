"""Sending a randomly generated verification code to a specific email using your own email.
Note: You have to manually enter the target email address then you manually enter the code they've sent"""

import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to generate a 6-digit random number
def generate_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])


# Function to send email
def send_email(to_email, code):
    """ Email credentials (replace with your actual credentials)
     Yahoo: smtp.mail.yahoo.com, Port 587 (TLS) / 465 (SSL)
     Gmail: smtp.gmail.com, Port 587 (TLS) / 465 (SSL)
     Hotmail/Outlook: smtp.office365.com, Port 587 (TLS) / 465 (SSL)
     iCloud: smtp.mail.me.com, Port 587 (TLS) / 465 (SSL)
     AOL: smtp.aol.com, Port 587 (TLS) / 465 (SSL) """
    smtp_server = 'smtp.mail.yahoo.com'
    smtp_port = 587
    email_user = 'your-account@yahoo.com'
    email_password = 'your password'
    """Note: You can't use your regular password here because this counts as a third party app. You need to get an APP PASSWORD.
     For yahoo you go to !!!MANAGE YOUR ACCOUNT -> SECURITY -> SCROLL DOWN -> HOW TO SIGN IN TO YAHOO -> APP PASSWORD"""

    subject = 'Your Verification Code'
    body = f'Your verification code is: {code}'

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(email_user, email_password)
            server.sendmail(email_user, to_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Function to verify the code
def verify_code(sent_code, sent_email):
    entered_code = input(f"Enter the verification code sent to {sent_email}: ")
    if entered_code == sent_code:
        print("Verification successful!")
    else:
        print("Incorrect code. Verification failed.")


# Main program
if __name__ == "__main__":
    # Generate a 6-digit code
    verification_code = generate_code()
    print(f"Generated code (for debugging): {verification_code}")  # Print the code for debugging

    # Get the customer's email address
    customer_email = input("Enter the customer's email address: ")

    # Send the code via email
    send_email(customer_email, verification_code)

    # Verify the code
    verify_code(verification_code, customer_email)