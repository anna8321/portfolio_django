from django.urls import path

from .views import (

    HomepageView, ContactUs,

)

app_name = 'blog'

urlpatterns = [

    path('', HomepageView.as_view(), name="blog-homepage"),
    path('contact/', ContactUs.as_view(), name="blog-contact"),
]
