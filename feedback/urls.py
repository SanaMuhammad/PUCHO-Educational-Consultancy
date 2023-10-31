from django.urls import path
from .views import feedback
from . import views
urlpatterns = [
    path('feedback/', feedback, name="feedback"),
]
