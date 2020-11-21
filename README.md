This is XRecognition

![Screenshot](assets/images/img.PNG)

XRecognition is a Multi-Lingual Handwritten Text Recognizer with Mathematical Experssion Recognition.

This is a web application made on FLASK Framework of Python and sqlite3 Database. For Front-end HTML,CSS, JavaScript is used.
The main program of the application is "application.py" which starts the program.
The web application asks user to upload any handwriiten scanned images (JPEG,PNG..etc)
and then it scans the text and expressions from the image and write it into a text file "output.txt" which then can be downloaded by the user.

To Recognise the text (OCR) - I have use VISION API from GCP (Google Cloud Vision API)

for VISION API - Make an account on GCP, Go to APIs section, search "VISION API" and then add it to your console.
How to use it? - https://cloud.google.com/vision use this link

When you have downloaded your GCP Credentials with Key in it, rename the file as "visionAPI.json", Transfer this file to the project folder.

To start the Web Application -

make sure you have these libraries installed in your terminal or VM

Package                  Version
------------------------ ----------
cachetools               4.1.0
certifi                  2020.4.5.1
chardet                  3.0.4
click                    7.1.1
cs50                     5.0.3
Flask                    1.1.2
Flask-Session            0.3.1
google-api-core          1.17.0
google-auth              1.14.0
google-cloud-vision      1.0.0
googleapis-common-protos 1.51.0
grpcio                   1.28.1
idna                     2.9
itsdangerous             1.1.0
Jinja2                   2.11.2
MarkupSafe               1.1.1
numpy                    1.18.3
panda                    0.3.1
pip                      20.0.2
protobuf                 3.11.3
pyasn1                   0.4.8
pyasn1-modules           0.2.8
pytz                     2019.3
requests                 2.23.0
rsa                      4.0
setuptools               46.1.3
six                      1.14.0
SQLAlchemy               1.3.16
sqlparse                 0.3.1
termcolor                1.1.0
urllib3                  1.25.9
Werkzeug                 0.16.0
wheel                    0.34.2


you can install any missing of them using - pip install LIBRARYNAME

To check your existing libraries you can use - pip list

Once you have done all this, Your application is Ready to Start.
Type "Flask run" on Terminal and your web application will start.

I have bought the domain and hosted this web application on xrecognition.in
Please check the website and also i have included the rest of the code here.

I am Utkarsh Choubey with my XRecognition and This is CS50.
