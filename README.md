PDF Crawler app
Description:
Basic Django app that accepts a pdf file through management command and saves all the URL found in the file in a relation databse and enable users to query data via endpoints

set up
- mkdir venv
- cd venv
- virtualenv -p pyhton3 .
- source bin/activate

Run install
- cd ../
- cd pdf_crawler
- pip install -r requirements.txt

Run management command to get and process file
 - python manage.py get_pdf <pdf_file>

Create super user
- python manage.py createsuperuser

Start Server:
python manage.py runserver

Endpoints
get all pdf files with url count
- /api/pdf-files/ 

get all urls with pdf file count
- /api/pdf-files/ 

get url count for a pdf file by file id
- /api/pdf-file/<file_id>

Test:
- python manage.py test

TODO:
- make management command callable from admin interface with file upload