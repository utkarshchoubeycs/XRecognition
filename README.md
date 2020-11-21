<h1><p align = "center">This is XRecognition </p> </h1>

![Screenshot](static/images/img.PNG)

<h3> XRecognition is a Multi-Lingual Handwritten Text Recognizer with Mathematical Experssion Recognition. </h3>

This is a web application made on FLASK Framework of Python and sqlite3 Database. For Front-end HTML,CSS, JavaScript is used.
The main program of the application is "application.py" which starts the program.
The web application asks user to upload any handwriiten scanned images (JPEG,PNG..etc)
and then it scans the text and expressions from the image and write it into a text file "output.txt" which then can be downloaded by the user.

To Recognise the text (OCR) - I have use VISION API from GCP (Google Cloud Vision API)

for VISION API - Make an account on GCP, Go to APIs section, search "VISION API" and then add it to your console.
How to use it? - https://cloud.google.com/vision use this link

When you have downloaded your GCP Credentials with Key in it, rename the file as "visionAPI.json", Transfer this file to the project folder.

To start the Web Application -

Make sure you have all the libraries mentioned in requirements.txt installed in your terminal or VM

- To check your existing libraries you can use - pip list
- you can install any missing of them using - pip install LIBRARYNAME
- or simply run pip install requirements.txt


Once you have done all this, Your application is Ready to run!
Type "Flask run" on Terminal and your web application will start.

I have bought the domain and hosted this web application on http://xrecognition.in
Please check the website and also i have included the rest of the code here.
