
from django.urls import path

from consultancyapp.views import *


urlpatterns = [
    path('',index.as_view(),name="index"),
    path('project',project.as_view(),name="project"),
]