import email
from dateutil import parser


def parse_email(email_message):
    # Extract the email message headers
    subject = email.header.decode_header(email_message['Subject'])

    if subject[0][1] is None:
        subject = subject[0][0]
    else:
        text = subject[0][0]
        encoding = subject[0][1]

        subject = text.decode(encoding)


    message_id = email.utils.parseaddr(email_message['Message-ID'])[1]
    date =  email_message['Date']
    date = parser.parse(date)
    date = date.timestamp()
    sender = email.utils.parseaddr(email_message['From'])[1]
    recipient = email.utils.parseaddr(email_message['To'])[1]
    body = None
    # Iterate through the message parts and extract the plain text body
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get_content_type() != 'text/plain':
            continue
        charset = part.get_content_charset()
        body = part.get_payload(decode=True).decode(charset)
        break
    # Return a dictionary containing the parsed email data
    return {
        'id': message_id,
        'date': date,
        'subject': subject,
        'sender': sender,
        'recipient': recipient,
        'body': body }