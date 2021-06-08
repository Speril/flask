from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import secure_filename
import predict

app = Flask(__name__)
app.debug = True

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ct')
def ct():
    return render_template("ct.html")


@app.route('/result')
def result():
    return render_template("result.html", Result=result)


@app.route('/map')
def map():
    return render_template("map.html")


@app.route('/news')
def news():
    return render_template("news.html")


@app.route('/signin')
def signin():
    return render_template("signin.html")


# 파일 업로드 처리 확인
@app.route('/fileupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        image = request.files['image']
        image.save('./Uploader/' + secure_filename(image.filename))
        image_path = './test/' + str(image.filename)
        transfer_img = predict.main(image_path)
    return 'file uploaded successfully!'


if __name__ == "__main__":
    app.run(debug=True)
