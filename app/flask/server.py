import sys
sys.path.insert(0,'../app/print')
from flask import Flask, render_template, request, redirect
import os 

#security 
from werkzeug.utils import secure_filename


#app
app = Flask(__name__)

#config path
#/home/pi/Desktop/python/Cloud-Printer-IoT/app/flask/static/images/uploads
app.config["IMAGE_UPLOADS"] = "/home/pi/Desktop/python/Cloud-Printer-IoT/app/flask/static/images/uploads"

#extentions
app.config["ALLOWED_EXTENSIONS"]=["PNG","JPG","JPEG","PDF","TXT"]

#function to check extebtions files
def allowed_files(filename):

    if not "." in filename:
        return False
    else:
        ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True

    else:
        return False

@app.route('/', methods=["GET","POST"])
def printcommando():

    if request.method == "POST":
        if request.files:

            file = request.files["file"]
    
    #checking 
            if file.filename == "":
                print("File is ready for print")
                return redirect(request.url)
            
            if not allowed_files(file.filename):
                print("That file extention is not allowed")
                return redirect(request.url)
            
            else:
                filename = secure_filename(file.filename)
        
            


            
            file.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            print("Image is saved")

            return redirect(request.url)

    return render_template('index.html')

@app.route('/succes', methods=['GET','POST'])
def succes():
    return render_template('succes.html')



#connection with server


if __name__  == "__main__":
	app.run(host='127.0.0.2',port="8000", debug=True)