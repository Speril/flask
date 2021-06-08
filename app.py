from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
app= Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/result')
def result():
   return render_template("result.html")

@app.route('/map')
def map():
   return render_template("map.html")

@app.route('/news')
def news():
   return render_template("news.html")

@app.route('/ct')
def ct():
   return render_template("ct.html")

@app.route('/signin')
def signin():
   return render_template("signin.html")

#파일 업로드 처리 확인
@app.route('/fileupload', methods = ['GET','POST'])
def upload_file():
       if request.method == 'POST':
            f = request.files['file']
            #저장 경로 + 파일명
            f.save('./Uploader/'+ secure_filename(f.filename))
            return 'file uploaded successfully!'

if __name__ == "__main__":
   app.run(debug=True)