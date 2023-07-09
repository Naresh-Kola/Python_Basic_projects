from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'pandukolanaresh@gmail.com'
email_password = 'xddu srjq sdsm djnw' # application-specific password
# How to Create Application-specific password
# First 2 step verification should be on
# Go to app passwords (https://myaccount.google.com/apppasswords)
# Create one Application-specific password and copy that password
# Use email_password as that copied message

email_receiver = '190040236ece@gmail.com'

subject = 'Dont forget to subscribe'

body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

