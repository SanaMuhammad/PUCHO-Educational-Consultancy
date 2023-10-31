from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("profiles.urls")),
    path("", include("university.urls")),
    path("", include("recommendation.urls")),
    path("", include("feedback.urls")),
]
