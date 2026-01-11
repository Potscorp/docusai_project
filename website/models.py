
from django.db import models
from django.contrib.auth.models import User

class MedicalReport(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    report_file = models.FileField(
    upload_to="medical_reports/",
    null=True,
    blank=True)

    analysis = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} - {self.uploaded_at.date()}"


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
