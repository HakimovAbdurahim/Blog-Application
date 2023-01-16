from django.core.mail import send_mail
from django.http import HttpResponse


def send_email(request):
    subject = 'Subject of the email'
    message = 'Body of the email'
    from_email = 'supercellid.4910@gmail.com'
    recipient_list = ['abdurahimxakimov163@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Email sent successfully')
