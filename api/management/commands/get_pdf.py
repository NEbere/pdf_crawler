from django.core.management.base import BaseCommand, CommandError
import PyPDF2
import os
import argparse
import requests

from api.models import PDFFile, PDFUrl


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def create_parser(self, *args, **kwargs):
        parser = super(Command, self).create_parser(*args, **kwargs)
        parser.formatter_class = argparse.RawTextHelpFormatter
        return parser

    def add_arguments(self, parser):
        parser.add_argument('pdf_file')

    def handle(self, *args, **options):
        import_pdf = options['pdf_file']
        with open(import_pdf, 'rb') as pdf_file:
            print(pdf_file, import_pdf)
            pdf = PyPDF2.PdfFileReader(pdf_file)

            pages = pdf.getNumPages()
            key = '/Annots'
            uri = '/URI'
            anchor = '/A'
            urls = []
            for page in range(pages):
                page_data = pdf.getPage(page)
                page_object = page_data.getObject()

                if key in page_object.keys():
                    annotations = page_object[key]
                    for annotation in annotations:
                        u = annotation.getObject()
                        if uri in u[anchor].keys():
                            url = u[anchor][uri]
                            if 'mailto:' not in url: # check for and remove emails
                                urls.append(u[anchor][uri])

                else:
                    print('key does not exist')
            if len(urls) != 0:
                try:
                    pdf_file, created = PDFFile.objects.get_or_create(
                        code =import_pdf,
                        defaults= {
                            'name':import_pdf,

                        } 
                    )
                    if created:
                        print('file details created for: ', pdf_file, created)
                except Exception as ex:
                    print('Error saving file details', str(ex))
            
                for file_url in urls:
                    url_alive = True
                    request = requests.get(file_url)
                    if request.status_code == 200:
                        url_alive = True
                    else:
                        url_alive = False
                    try:
                        pdf = PDFFile.objects.get(code=import_pdf)
                        pfd_url, created = PDFUrl.objects.get_or_create(
                            pdf=pdf,
                            url_link=file_url,
                            url_alive=url_alive
                        )
                        if created:
                            print('url created: ', pfd_url)
                    except Exception as ex:
                        print('Error saving file url', str(ex))
            else:
                print("No links in PDF file")