import os, re, glob
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow.keras.applications import vgg19

def Dataization(img_path):
    image_w = 112
    image_h = 112
    ff = np.fromfile(img_path, np.uint8)
    img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

    img = cv2.resize(img, None, fx=image_w / img.shape[1], fy=image_h / img.shape[0])
    return (img/256)


def main(img_path):
    image_dir = './static/img/test/'
    categories = ['COVID', 'Non-COVID']
    src = []
    name = []
    test = []

    for file in os.listdir(img_path):
        if file.find('.png') is not -1:
            src.append(img_path + file)
            name.append(file)
            test.append(Dataization(img_path + file))

    test = np.array(test)
    model = load_model('C:/Users/175767/PycharmProjects/flask/model/COVIDMD.h5')
    predict = model.predict_classes(test)

    for i in range(len(test)):
        result = (name[i] + " : , Predict : " + str(categories[predict[i]]))

    return result


if __name__ == "__main__":
    main()
