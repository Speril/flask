from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import secure_filename
import predict
import os, re, glob

app = Flask(__name__)
app.debug = True


def root_path():
    '''root 경로 유지'''
    real_path = os.path.dirname(os.path.realpath(__file__))
    sub_path = "\\".join(real_path.split("\\")[:-1])
    return os.chdir(sub_path)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ct')
def ct():
    return render_template("ct.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    image_dir = 'C:/Users/175767/PycharmProjects/flask/static/img/'
    if request.method == 'POST':
        root_path()

        image = request.files['image']
        image.save('./flask/static/img/' + str(image.filename))
        image_path = (image_dir+str(image.filename))
        image_type = str(image.filename).split('.')[1]
        # img file
        if image_type in ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG']:
            print('Type is Image')
            pre_result = predict.main()
            # detected_img_path = '../static/img/' + str(detected_img.split('/')[-1])
    return render_template("result.html", Result=pre_result, image_file=image_path)


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
# @app.route('/fileupload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         image = request.files['image']
#         image.save('./Uploader/' + secure_filename(image.filename))
#         image_path = './test/' + str(image.filename)
#         transfer_img = predict.main(image_path)
#         transfer_img_path = str(transfer_img.split('/')[-1])
#     return render_template("result.html", Result=result)

if __name__ == "__main__":
    app.run(debug=True)
