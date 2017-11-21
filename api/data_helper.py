from api.models import PDFFile, PDFUrl

class DataHelper():
    def create_pdf_file(self):
        self.pdf_file = PDFFile.objects.create(
            name='test_pdf_file',
            code='test_pdf_file'
        )

        self.test_url_1 = PDFUrl.objects.create(
            pdf=self.pdf_file,
            url_link='google.com'
        )

        self.test_url_2 = PDFUrl.objects.create(
            pdf=self.pdf_file,
            url_link='gmail.com'
        )
