from django.db import models
from django.utils import timezone

# Build the contact form using the inheritance and ORM
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
# I'll create an ENUM regarding to multi-section part on index.html

    DEPARTMENTS = [
        ('MF', 'Manufacturing'),
        ('SH', 'Shipping'),
        ('AD', 'Administration'),
        ('HR', 'Human Resources')
    ]
    
    dept = models.CharField(max_length=2, choices=DEPARTMENTS, default=DEPARTMENTS[3][0])
    