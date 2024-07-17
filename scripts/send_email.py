import gemini
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

gemini.api_key = "AIzaSyAYjwOuigc03kLqMBlKwQeyrlW9PmW4n60"

def generate_email_content_with_gemini(data):
    """Generates email subject and body using Gemini LLM."""
    prompt = f"Generate a comprehensive sales email based on the following data: {data}"
    response = gemini.ChatCompletion.create(
        model="gemini-llm",  # Choose an appropriate Gemini LLM model
        messages=[
            {"role": "system", "content": "You are an expert email writer."},
            {"role": "user", "content": prompt}
        ]
    )
    email_content = response.choices[0].text
    subject, body = email_content.split('\n', 1)
    return subject.strip(), body.strip()

def send_email(smtp_config, recipient_emails, data, attachment_path):
    try:
        subject, body = generate_email_content_with_gemini(data)

        msg = MIMEMultipart()
        msg['From'] = smtp_config['sender_email']
        msg['To'] = ", ".join(recipient_emails)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=attachment_path)
            part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
            msg.attach(part)

        server = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
        server.starttls()
        server.login(smtp_config['sender_email'], smtp_config['sender_password'])
        server.sendmail(smtp_config['sender_email'], recipient_emails, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
