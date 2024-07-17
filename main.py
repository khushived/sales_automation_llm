from scripts.convo_agent import SalesReportAgent

smtp_config = {
    'server': 'smtp.gmail.com',
    'port': 587,
    'sender_email': 'gliterry87@gmail.com',
    'sender_password': 'heyther@87'
}

recipient_emails = ['khushived6@gmail.com']

agent = SalesReportAgent(
    data_path='data/sales_data.xlsx',
    template_path='templates/report_template.html',
    output_path='reports/daily_sales_report.pdf',
    smtp_config=smtp_config,
    recipient_emails=recipient_emails
)

def main():
    while True:
        user_request = input("How can I assist you? ")
        if 'exit' in user_request.lower().strip():
            break
        agent.process_request(user_request)

if __name__ == "__main__":
    main()
