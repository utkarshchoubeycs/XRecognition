import os,io
import ssl
import json
import requests
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session,send_file
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from  google.cloud import vision
from google.cloud.vision import types
import uuid



#certificate_errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

app.jinja_env.filters["usd"] = usd



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config['UPLOAD_FOLDER'] = "UPLOADS"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'visionAPI.json'

client = vision.ImageAnnotatorClient()



#filename = ""
@app.route("/")
def ok():
    #id = session["user_id"]
    return render_template("index.html")
   
@app.route('/upload', methods = ['POST'])
def success():
    if request.method == 'POST':
    
        
        global filename
        f = request.files['file']
        if f.filename == "" :
                   return redirect("/error")
        f.save(f.filename)
        filename = f.filename
        
        
   
        
        return render_template("success.html", name = f.filename)



@app.route("/Recognised", methods = ['GET'])
def main():
    if request.method == 'GET':
        """Detects document features in an image."""

        #f = request.files['file']
        #f.save(f.filename)
        try :
            doc = filename
        except :
             return redirect("/error")
    

        try :
            with io.open(doc, 'rb') as image_file:
                content = image_file.read()
        except :
            return redirect("/error")

        image = vision.types.Image(content=content)

        response = client.document_text_detection(image=image)

        docText = response.full_text_annotation.text
        f= open("output.txt","w+")
        f.write(docText)
        f.close()
        message = "Recognition Successful!!"
        if response.error.message:
            message = "Recognition Failed! Try again."
        
       
        os.remove(filename)
    
        return render_template("recognition.html", name = doc, message = message, file = docText)

@app.route("/error")
def error():
    msg = "Select the image first!"
    return render_template("index.html",msg = msg)
      
      
@app.route("/Download")
def Download():
    #os.remove(filename)
    return send_file("output.txt", as_attachment=True)
    
@app.route("/about")
def about():
    return render_template("layout.html")
#app.run(debug=True)
