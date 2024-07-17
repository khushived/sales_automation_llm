import gemini
import pandas as pd
from scripts.generate_report import generate_report
from scripts.send_email import send_email
from scripts.extract_data import extract_data_with_llm

gemini.api_key = "AIzaSyAYjwOuigc03kLqMBlKwQeyrlW9PmW4n60"

class SalesReportAgent:
    def __init__(self, data_path, template_path, output_path, smtp_config, recipient_emails):
        self.data_path = data_path
        self.template_path = template_path
        self.output_path = output_path
        self.smtp_config = smtp_config
        self.recipient_emails = recipient_emails
    
    def extract_data(self):
        data = extract_data_with_llm(self.data_path)
        return data
    
    def generate_report(self, data):
        report_content = generate_report_with_llm(data)
        generate_report(report_content, self.template_path, self.output_path)
    
    def send_report(self):
        subject = "Daily Sales Report"
        body = "Please find attached the daily sales report."
        send_email(self.smtp_config, self.recipient_emails, subject, body, self.output_path)
    
    def process_request(self, request):
        if 'send report' in request.lower():
            data = self.extract_data()
            if data is not None:
                self.generate_report(data)
                self.send_report()
            else:
                print("Failed to extract data from the spreadsheet.")
        else:
            print("Sorry, I didn't understand your request.")
