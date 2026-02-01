from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings

from .models import WorkshopRegistration
from .serializers import WorkshopRegistrationSerializer
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "API is live"})

class RegisterStudentView(APIView):
    def post(self, request):
        serializer = WorkshopRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            registration = serializer.save()

            subject = "Workshop Registration Successful ✅"
            message = f"""
Hello {registration.name},

Your registration for the Workshop is successful.

Details:
Name: {registration.name}
Email: {registration.email}
Branch: {registration.branch}
Year: {registration.year}
Hosteller: {"Yes" if registration.hosteller else "No"}
Student No: {registration.student_no}

Thank you!
Workshop Team
            """

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[registration.email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response(
                    {
                        "message": "Registered but email failed.",
                        "email_error": str(e),
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {"message": "Registration successful and email sent.", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListRegistrationsView(APIView):
    def get(self, request):
        qs = WorkshopRegistration.objects.all().order_by("-created_at")
        serializer = WorkshopRegistrationSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)