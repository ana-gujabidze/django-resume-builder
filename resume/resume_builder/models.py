from django.db import models
from django.urls import reverse
from django.utils import timezone


class Resume(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    desired_position = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    professional_summary = models.TextField(null=True, blank=True)
    user_img = models.ImageField(upload_to="images/", null=True, blank=True)
    references = models.TextField(null=True, blank=True)
    career_obj = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    job_1_description = models.TextField(null=True, blank=True)
    job_1_start_dt = models.DateTimeField(null=True, blank=True)
    job_1_end_dt = models.DateTimeField(null=True, blank=True)
    job_2_description = models.TextField(null=True, blank=True)
    job_2_start_dt = models.DateTimeField(null=True, blank=True)
    job_2_end_dt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
