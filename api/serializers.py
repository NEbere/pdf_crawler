from rest_framework import serializers
from .models import PDFFile, PDFUrl

class PDFFileSerializer(serializers.ModelSerializer):
    num_urls = serializers.IntegerField()
    class Meta:
        model = PDFFile
        fields = [
            'id', 'name', 'code', 'date_created', 'num_urls'
        ]

class PDFUrlSerializer(serializers.ModelSerializer):
    num_pdf = serializers.IntegerField()
    class Meta:
        model = PDFUrl
        fields = [
            'id', 'url_link', 'url_alive', 'date_created', 'num_pdf'
        ]

class PDFFileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFUrl
        fields = [
            'id', 'url_link', 'url_alive', 'date_created',
        ]

