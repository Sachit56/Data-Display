from django.urls import path
from .views import *

urlpatterns = [
    path('upload/',upload,name='upload')
]
