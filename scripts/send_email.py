from transformers import pipeline

def generate_email_content_with_transformers(data):
    """Generates email subject and body using Transformers LLM."""
    prompt = f"Generate a comprehensive sales email based on the following data: {data}"

    # Initialize the transformer pipeline for text generation
    model_name = "distilgpt2"  # Example model, you can choose based on your needs
    generator = pipeline("text-generation", model=model_name)

    # Generate email content based on the prompt
    email_content = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    subject, body = email_content.split('\n', 1)
    
    return subject.strip(), body.strip()

def send_email(smtp_config, recipient_emails, data, attachment_path):
    try:
        subject, body = generate_email_content_with_transformers(data)

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
