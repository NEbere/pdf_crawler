from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'pdf-files', views.PDFFileListView.as_view(), name='pdf-files-list'),
    url(r'pdf-urls', views.PDFUrlListView.as_view(), name='pdf-url-list'),
    url(r'pdf-file/(?P<pdf_file_id>[-\w\d]{2,10})/?$', views.PDFFileDetailView.as_view(), name='pdf-file-detail'),
]