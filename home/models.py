from django.db import models
from django.utils import timezone

# Build the contact form using the inheritance and ORM
class Contact(models.Model):
    user_id = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
# I'll create an ENUM regarding to multi-section part on index.html

    LIST = [
        ('Ka', "Karakter Analizi"),
        ('DD', "Duygusal Durumu"),
        ('HO', "Hobileri"),
        ('ID', "İlişki Durumu")
    ]
    
    list = models.CharField(max_length=2, choices=LIST, default=LIST[3][0])
    