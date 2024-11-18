from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from datetime import datetime

WORKING_RECEIVER_EMAIL = 'gtlyco205@gmail.com'  # Replace with your actual email address

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Render the email content
            email_subject = f"New Contact Form Submission from {name}"
            email_body = render_to_string('emails/email_template.html', {
                'name': name,
                'email': email,
                'message': message,
                'current_year': datetime.now().year
            })

            try:
                email_message = EmailMessage(
                    email_subject,
                    email_body,
                    WORKING_RECEIVER_EMAIL,  # From email
                    [WORKING_RECEIVER_EMAIL]  # To email
                )
                email_message.content_subtype = 'html'  # Mark content as HTML
                email_message.send()
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                print(f"Error: {e}")  # Print the error for debugging
                messages.error(request, 'There was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'All fields are required.')

        # Redirect to the same page to prevent form resubmission
        return redirect('home')  # Replace 'home' with your view name or path

    return render(request, 'pages/index.html')
