import sys
sys.path.insert(0,'../app/print')
from flask import Flask, render_template, request, redirect,send_from_directory, abort
import os 

#security 
from werkzeug.utils import secure_filename


#app
app = Flask(__name__)

#config path
#/home/pi/Desktop/python/Cloud-Printer-IoT/app/flask/static/images/uploads
app.config["IMAGE_UPLOADS"] = "/home/pi/Desktop/python/Cloud-Printer-IoT/app/flask/static/images/uploads"

#extentions
app.config["ALLOWED_EXTENSIONS"]=["PNG","JPG","JPEG","PDF","TXT", "DOC", "DOCX"]


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

            print("file is saved")
            
            req = request.form

            printerkleurenpatroon = req.get("printerkleurenpatroon")
            afdrukkant = request.form["afdrukkant"]
            formaat = request.form["formaat"]

            print(printerkleurenpatroon,afdrukkant,formaat)

            return redirect(request.url)

         

    return render_template('index.html')


"""
string:
int:
float:
path:
uuid:
"""

@app.route('/succes/<string:filename>')

#get the files
def get_file(filename):

    #try and except -> send a file 
    try:
        return send_from_directory(app.config["IMAGE_UPLOADS"],filename=filename, as_attachment=False)

    except FileNotFoundError:
        abort(404)




@app.route('/succes', methods=['GET','POST'])
def succes():
    return render_template('succes.html')






  





#connection with server


if __name__  == "__main__":
    port = int(os.environ.get("PORT", 8080))
    
app.run(host='127.0.0.1',port=port, debug=True)
    