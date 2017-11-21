from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class PDFFile(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=timezone.now())


class PDFUrl(models.Model):
    pdf = models.ForeignKey(PDFFile, on_delete=models.CASCADE, related_name='pdf_file', related_query_name='pdf_file')
    url_link = models.CharField(max_length=200)
    url_alive = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now())