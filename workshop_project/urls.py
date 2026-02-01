from django.contrib import admin
from django.urls import path, include
from registration.views import health_check  # import the view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("registration.urls")),
    path("", health_check),  # ye root URL ke liye
]