from django.shortcuts import render
from django.core.mail import send_mail
from .models import Message
from django.conf import settings

def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']

        # Save to database
        Message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )

        # Send email to YOU
        send_mail(
            subject=f"New Hiring Message: {subject}",
            message=f"""
Name: {name}
Email: {email}

Message:
{message_text}
            """,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        success = True

    return render(request, 'contact/contact.html', {'success': success})
