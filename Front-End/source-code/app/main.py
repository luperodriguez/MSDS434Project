from flask import Flask
from flask import render_template
import os


app = Flask(__name__)



IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route("/")
def Display_IMG():
    IMG_LIST = os.listdir('static/IMG')
    IMG_LIST = ['IMG/' + i for i in IMG_LIST]
    return render_template("index.html", imagelist=IMG_LIST)




if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
