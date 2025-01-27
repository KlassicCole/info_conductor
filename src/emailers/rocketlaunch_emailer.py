from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT

def send_rocketlaunch_email(launch_data):
    """
    Send an HTML email with formatted rocket launch data.
    """
    # HTML Email Template
    email_content = """\
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border: 1px solid #ddd;
                    border-radius: 10px;
                }}
                .header {{
                    background-color: #004080;
                    color: white;
                    padding: 15px;
                    text-align: center;
                    font-size: 24px;
                    border-radius: 10px 10px 0 0;
                }}
                .launch-item {{
                    margin: 20px 0;
                    padding: 15px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background-color: #f7f7f7;
                }}
                .launch-title {{
                    font-weight: bold;
                    font-size: 18px;
                    color: #004080;
                }}
                .launch-detail {{
                    margin: 5px 0;
                    color: #555;
                }}
                .footer {{
                    text-align: center;
                    font-size: 12px;
                    color: #777;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    Upcoming Rocket Launches
                </div>
                {launch_items}
                <div class="footer">
                    This is an automated email. Please do not reply.
                </div>
            </div>
        </body>
    </html>
    """

    # Generate formatted launch data
    launch_items = ""
    for launch in launch_data:
        mission = launch.get('mission', 'Unknown Launch')
        date = launch.get('date', 'TBD')
        location = launch.get('location', 'Unknown')
        vehicle = launch.get('vehicle', 'Unknown')
        description = launch.get('description', 'No description available.')

        launch_items += f"""
        <div class="launch-item">
            <div class="launch-title">{mission}</div>
            <div class="launch-detail"><strong>Date:</strong> {date}</div>
            <div class="launch-detail"><strong>Location:</strong> {location}</div>
            <div class="launch-detail"><strong>Vehicle:</strong> {vehicle}</div>
            <div class="launch-detail"><strong>Description:</strong> {description}</div>
        </div>
        """

    # Format the email content
    email_body = email_content.format(launch_items=launch_items)

    # Set up the email
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL
    msg["To"] = EMAIL  # Replace with the recipient's email
    msg["Subject"] = "Upcoming Rocket Launches"
    msg.attach(MIMEText(email_body, "html"))

    # Send the email
    try:
        import smtplib
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
