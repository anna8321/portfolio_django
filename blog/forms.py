from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'company', 'email', 'content', 'phone')

        def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)

