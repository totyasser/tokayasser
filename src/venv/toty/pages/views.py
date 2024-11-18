# portfolio/views.py

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from datetime import datetime
from .models import Testimonial, Education, Experience, Skill, Portfolio
import logging

WORKING_RECEIVER_EMAIL = 'gtlyco205@gmail.com'  # Replace with your actual email address
logger = logging.getLogger(__name__)  # Set up a logger for better debugging

def send_email(name, email, message):
    """Helper function to send an email."""
    try:
        email_subject = f"New Contact Form Submission from {name}"
        email_body = render_to_string('emails/email_template.html', {
            'name': name,
            'email': email,
            'message': message,
        })

        email_message = EmailMessage(
            email_subject,
            email_body,
            WORKING_RECEIVER_EMAIL,  # From email
            [WORKING_RECEIVER_EMAIL]  # To email
        )
        email_message.content_subtype = 'html'  # Mark content as HTML
        email_message.send()
        return True
    except Exception as e:
        logger.error(f"Error sending email: {e}")  # Log the error
        return False

def home(request):
    """View for rendering the homepage."""
    testimonials = Testimonial.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    portfolios = Portfolio.objects.all()

    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate the input
        if not all([name, email, message]):
            messages.error(request, 'All fields are required.')
            return redirect('home')

        # Send email
        if send_email(name, email, message):
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return redirect('home')  # Prevent form resubmission

    # Render the homepage with all necessary data
    context = {
        'testimonials': testimonials,
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
        'portfolios': portfolios,
    }
    return render(request, 'pages/index.html', context)
