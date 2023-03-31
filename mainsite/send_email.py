import smtplib
from email.message import EmailMessage


def send_mail(to, subject, msg):
    email = EmailMessage()
    email['from'] = 'mohammadisaeedir@gmai.com'
    email['to'] = to
    email['subject'] = subject
    email.set_content(msg)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('mohammadisaeedir@gmail.com', 'Sm@220!93067')
        smtp.send_message(email)
