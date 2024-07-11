from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50)
    message = models.TextField()
    #agree_terms = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'contacts'

class UserCredentials(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username