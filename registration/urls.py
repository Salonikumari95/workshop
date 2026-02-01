from django.urls import path
from .views import RegisterStudentView, ListRegistrationsView

urlpatterns = [
    path("register/", RegisterStudentView.as_view(), name="register-student"),
    path("registrations/", ListRegistrationsView.as_view(), name="list-registrations"),
]