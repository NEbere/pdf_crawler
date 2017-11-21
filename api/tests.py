from django.test import TestCase
from api.data_helper import DataHelper
from django.urls import reverse
from rest_framework import status
from nose.tools import eq_

from api.models import PDFFile, PDFUrl

class ModelTest(TestCase):
    def setUp(self):
        self.db_data = DataHelper()

    def tearDown(self):
        pass

    def test_pdf_file_model(self):
        self.db_data.create_pdf_file()
        self.pdf_file = self.db_data.pdf_file
        self.assertTrue(isinstance(self.pdf_file, PDFFile))

        code = self.pdf_file._meta.get_field('code')
        name = self.pdf_file._meta.get_field('name')
        self.assertNotEqual(code, name)


    def test_pdf_url_model(self):
        self.db_data.create_pdf_file()
        self.test_url_1 = self.db_data.test_url_1
        self.test_url_2 = self.db_data.test_url_2

        self.assertTrue(isinstance(self.test_url_1, PDFUrl))
        self.assertTrue(isinstance(self.test_url_2, PDFUrl))
    
    def test_pdf_file_url_response(self, url_string, **kwargs):
        url = reverse(url_string, kwargs=kwargs)
        return self.client.get(url)

    def test_pdf_files_url_exists(self):
        response = self.client.get('/api/pdf-files/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_pdf_links_url_exists(self):
        response = self.client.get('/api/pdf-urls/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pdf_files_url_accessible_by_name(self):
        response = self.client.get(reverse('pdf-files-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_pdf_links_url_accessible_by_name(self):
        response = self.client.get(reverse('pdf-url-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list_view(self):
        self.db_data.create_pdf_file()
        response = self.test_pdf_file_url_response(
            'pdf-files-list'
        )
        self.assertNotEqual(response, None)
        eq_(response.status_code, status.HTTP_200_OK)

