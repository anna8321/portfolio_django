from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Project

from django.apps import apps
Blog = apps.get_model('blog', 'Blog')


class ProjectIndex(ListView):
    model = Project
    template_name = "project_index.html"

    def index_project(self, **kwargs):
        index = super().index_project(**kwargs)
        return index


class ProjectShow(DetailView):
    model = Project
    template_name = "project_show.html"

    def show_project(self, **kwargs):
        show = super().show_project(**kwargs)
        qs = self.get_object()
        qs.visit_counter += 1
        qs.save()
        return show


