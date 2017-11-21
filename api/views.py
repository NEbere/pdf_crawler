from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.generics import ListAPIView

from django.db.models import Count


from .serializers import PDFFileSerializer, PDFUrlSerializer, PDFFileDetailSerializer
from api.models import PDFFile, PDFUrl

# Create your views here.
class PDFFileListView(ListAPIView):
    queryset = PDFFile.objects.annotate(num_urls=Count('pdf_file'))
    serializer_class = PDFFileSerializer

class PDFUrlListView(ListAPIView):
    queryset = PDFUrl.objects.annotate(num_pdf=Count('pdf'))
    serializer_class = PDFUrlSerializer

class PDFFileDetailView(ListAPIView):
    pdf_urls = PDFUrl.objects.all()
    serializer_class = PDFFileDetailSerializer

    def get_queryset(self):
        pdf_file_id = self.kwargs.get('pdf_file_id')

        if pdf_file_id:
            pdf_urls = PDFUrl.objects.filter(pdf=pdf_file_id)

        return pdf_urls
    

