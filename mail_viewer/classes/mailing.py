import imaplib
import email
import time
from modules.parsers import parse_email
import requests


class EmailProcessor:
    def __init__(self, username, password, server, port, folder):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.folder = folder
        self.imap_conn = None

    def connect(self):
        # Connect with the server
        self.imap_conn = imaplib.IMAP4_SSL(self.server, self.port)
        self.imap_conn.login(self.username, self.password)

        # Select the inbox folder
        self.imap_conn.select(self.folder)

    def disconnect(self):
        # Close the connection
        if self.imap_conn:
            self.imap_conn.close()
            self.imap_conn.logout()

    def process_emails(self, criteria, api_url):
        # Search for new mails
        status, email_id = self.imap_conn.search(None, criteria)

        for id in email_id[0].split():
            status, email_data = self.imap_conn.fetch(id, "(RFC822)")
            raw_email = email_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            email_message = parse_email(email_message)

            mail_id = email_message['id']
            mail_date = email_message['date']
            client_email = email_message['sender']
            email_body = email_message['body']

            # Share email data with API
            data = {
                'date': mail_date,
                'sender': client_email,
                'body': email_body
            }

            print(data)
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                print(f'Successfully shared email to API')
            else:
                print(f'Error sharing email with id {mail_id} to API. Status code: {response.status_code}')

    def run(self, api_url, criteria, delay_seconds=10):
        while True:
            try:
                self.connect()
                self.process_emails(criteria = criteria, api_url= api_url)
            except Exception as e:
                print(f'Error processing emails: {str(e)}')
            finally:
                self.disconnect()
            time.sleep(delay_seconds)
