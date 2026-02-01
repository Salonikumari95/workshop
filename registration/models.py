from django.db import models

# Create your models here.
from django.db import models

class WorkshopRegistration(models.Model):
    BRANCH_CHOICES = [
        ("CSE", "CSE"),
        ("IT", "IT"),
        ("ECE", "ECE"),
        ("EEE", "EEE"),
        ("ME", "ME"),
        ("CE", "CE"),
        ("OTHER", "OTHER"),
    ]

    YEAR_CHOICES = [
        (1, "1st Year"),
        (2, "2nd Year"),
        (3, "3rd Year"),
        (4, "4th Year"),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES, default="OTHER")
    hosteller = models.BooleanField(default=False)
    student_no = models.CharField(max_length=50, unique=True)
    year = models.IntegerField(choices=YEAR_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"