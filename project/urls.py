from django.urls import path


from .views import (

    ProjectIndex, ProjectShow,

)

app_name = 'project'

urlpatterns = [

    path('', ProjectIndex.as_view(), name="project-index"),
    path('<str:slug>/', ProjectShow.as_view(), name="project-show"),
]