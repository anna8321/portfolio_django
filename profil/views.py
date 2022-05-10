from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Profile


class ProfileView(ListView):
    model = Profile
    template_name = "about_me.html"

    def get_profile (self, **kwargs):
        page = super().get_profile(**kwargs)
        return page


