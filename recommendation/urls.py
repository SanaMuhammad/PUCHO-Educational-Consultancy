from django.urls import path
from .views import recommendation, savedlinks, aboutus
from . import views
urlpatterns = [
    path('recommendation/', recommendation, name="recommendation"),
    path('savedlinks/', savedlinks, name="savedlinks"),
    path('aboutus/', aboutus, name="aboutus"),

]
