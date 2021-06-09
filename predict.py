import os, re, glob
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow.keras.applications import vgg19

def Dataization(img_path):
    image_w = 112
    image_h = 112
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)


def main():
    image_dir = 'C:\\Users\\175767\\PycharmProjects\\flask\\static\\img\\test\\'
    categories = ['COVID', 'Non-COVID']
    src = []
    name = []
    test = []

    for file in os.listdir(image_dir):
        if file.find('.png') is not -1:
            src.append(image_dir + file)
            name.append(file)
            test.append(Dataization(image_dir + file))

    test = np.array(test)
    model = load_model('C:/Users/175767/PycharmProjects/flask/model/COVIDMD.h5')
    predict = model.predict_classes(test)

    for i in range(len(test)):
        result = (name[i] + " : , Predict : " + str(categories[predict[i]]))

    return result


if __name__ == "__main__":
    main()
