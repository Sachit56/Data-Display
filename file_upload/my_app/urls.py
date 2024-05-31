from django.urls import path
from .views import summary,upload

urlpatterns = [
    path('upload/',upload,name='upload'),
    path('summary/',summary,name='summary')
]
