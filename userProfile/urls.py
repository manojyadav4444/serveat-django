from django.urls import path
from .views import CreateProfile

urlpatterns=[
    path('register/', CreateProfile.as_view()),
]