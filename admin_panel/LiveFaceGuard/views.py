from django.shortcuts import render
from .models import Alert, Person
from django.core.mail import send_mail
from django.utils.timezone import now

def send_alert(person_id, location):
    try:
        # Fetch the person's details
        person = Person.objects.get(id=person_id)

        # Create an alert in the database
        alert = Alert.objects.create(person=person, location=location, timestamp=now())

        # Email configuration
        subject = f"ALERT: {person.name} Detected"
        message = f"""
        {person.name} was detected at {location} on {alert.timestamp}.
        Please take immediate action.
        """
        sender_email = "viobunch@gmail.com"
        recipient_email = "dasviolina51@gmail.com"  # Replace with dynamic recipient logic if needed

        # Send the email
        send_mail(
            subject,
            message,
            sender_email,
            [recipient_email],
            fail_silently=False,  # Ensures errors are raised if email fails
        )

        # Mark the alert as sent and save it
        alert.is_sent = True
        alert.save()

        print("Alert sent successfully!")

    except Person.DoesNotExist:
        print(f"Error: Person with ID {person_id} does not exist.")
    except Exception as e:
        print(f"Error sending alert:{e}")

    