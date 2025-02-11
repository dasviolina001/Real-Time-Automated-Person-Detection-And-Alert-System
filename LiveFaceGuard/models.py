from django.db import models

class LiveFaceGuard(models.Model):
    # Define the fields for your model here
    name = models.CharField(max_length=100)
    # Add more fields as required

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=50)  # Name of the person
    photo = models.ImageField(upload_to='photos/')  # Photo upload location
    details = models.TextField(null=True, blank=True)  # Additional details

    def __str__(self):  # Corrected this to __str__
        return self.name  # Display name in the admin panel

#class Alert(models.Model):
    #person = models.ForeignKey('Person', on_delete=models.CASCADE)  # Link to detected person
    #location = models.CharField(max_length=255)  # Location of detection
    #timestamp = models.DateTimeField(auto_now_add=True)  # When detection occurred
    #is_sent = models.BooleanField(default=False)  # Has the alert been sent?

    #def __str__(self):  # Corrected this to __str__
        #return f"Alert for {self.person.name} at {self.location} on {self.timestamp}"
