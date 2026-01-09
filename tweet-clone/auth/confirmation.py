import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from core.db_settings import execute_query



def send_email(recipient_email, subject, body):
    """
    Send a text email using Gmail SMTP server

    Args:
        recipient_email: Recipient's email address
        subject: Email subject
        body: Email body text
    """

    # 🔐 Sender email credentials
    sender_email = "sanjarbekwork@gmail.com"
    sender_password = "ukjc bzah lgvv qvxh"

    try:

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        print("✅ Email muvaffaqiyatli yuborildi")

    except Exception as e:
        print("❌ Email yuborishda xatolik:", e)
    # Validate credentials


    EMAIL_USER = "sanjarbekwork@gmail.com"
    EMAIL_PASS = "ukjc bzah lgvv qvxh"

    # Create message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server
    server = None
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        # Send email
        server.send_message(msg)
        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False
    finally:
        if server:
            server.quit()


def generate_code(user_email):
    code = str(random.randint(100000, 999999))
    query = "SELECT * FROM codes WHERE code = (%s)"
    params = (code,)
    result = execute_query(query=query, params=params, fetch="one")
    if result:
        return generate_code(user_email)
    query1 = "INSERT INTO codes (email, code) VALUES (%s, %s)"
    params1 = (user_email, code)
    if execute_query(query=query1, params=params1):
        print("Code sent to your email")
        print("Code", code)
        return code
    print("Something went wrong, try again later")
    return None