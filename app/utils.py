import smtplib
from email.message import EmailMessage
import uuid
from app.models import db

def send_reset_email(user):
    token = str(uuid.uuid4())

    user.verification_token = token
    db.session.commit()

    msg = EmailMessage()
    msg["Subject"] = "Επαναφορά Κωδικού"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = user.email
    msg.set_content(
        f"Πάτησε στον σύνδεσμο για να αλλάξεις τον κωδικό σου:\n\nhttp://127.0.0.1:5000/reset-password?token={token}"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("your_email@gmail.com", "your_app_password")
        smtp.send_message(msg)
