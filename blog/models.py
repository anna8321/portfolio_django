from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.CharField(max_length=500)
    phone = PhoneNumberField(unique = True, null = False, blank = False)

    def __str__(self):
        return str(self.contact) or ""

    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)
