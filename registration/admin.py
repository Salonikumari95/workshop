from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WorkshopRegistration

@admin.register(WorkshopRegistration)
class WorkshopRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "branch", "year", "hosteller", "student_no", "created_at")
    search_fields = ("name", "email", "student_no")
    list_filter = ("branch", "year", "hosteller")