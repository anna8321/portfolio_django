from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500, default='')
    technology = models.CharField(max_length=300, default=0)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to="static/images/project", blank='True', null=True)
    visit_counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.title) or ""

    def get_title_display(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('project:project-show',
                       kwargs={'slug': self.slug}
                       )

    def save(self, *args, **kwargs):
        if self.slug:
            super(Project, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title + get_random_string(9))
            super(Project, self).save(*args, **kwargs)
