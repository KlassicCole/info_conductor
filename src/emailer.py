import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT

def send_email(cards_by_commander):
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg['Subject'] = 'New Commander Card Recommendations'

    # Build the email body by grouping recommendations per commander
    email_body = "<h2>New Commander Card Recommendations</h2>"

    for commander, cards in cards_by_commander.items():
        if cards:
            email_body += f"<h3>{commander}</h3><ul>"
            for card in cards:
                email_body += f"<li>{card['name']}</li>"
            email_body += "</ul>"

    if email_body == "<h2>New Commander Card Recommendations</h2>":
        email_body += "<p>No new recommendations at this time.</p>"

    # Attach the formatted HTML email body
    msg.attach(MIMEText(email_body, 'html'))

    try:
        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, msg.as_string())

        print("Email sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")