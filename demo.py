import os 
print(os.environ.get('MAIL_USER'))

from django.core.mail import EmailMessage
from django.conf import settings

settings.configure(DEBUG=True)


email = EmailMessage(
    'Hello',
    'Body goes here',
    'myemail@outlook.com',  # This should match with EMAIL_HOST_USER
    ['to@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)

print(email.message().items())  # This will print the headers
