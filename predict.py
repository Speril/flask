import os, re, glob
import cv2
import numpy as np
from tensorflow.keras.models import load_model

image_dir = '/test/'
categories = ['COVID', 'Non-COVID']


# def preprocess_image(image_path):
# 	img = load_img(image_path, target_size=(img_height, img_width)) # (400, 381)
# 	img = img_to_array(img) 			# (400, 381, 3)
# 	img = np.expand_dims(img, axis=0) 	# (1, 400, 381, 3)
# 	img = vgg19.preprocess_input(img)
#
# 	return img


def Dataization(img_path):
    image_w = 112
    image_h = 112
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w / img.shape[1], fy=image_h / img.shape[0])
    return img / 256


def main(image_path):
    src = []
    name = []
    test = []

    for file in os.listdir(image_path):
        if file.find('.png') is not -1:
            src.append(image_dir + file)
            name.append(file)
            test.append(Dataization(image_dir + file))

    test = np.array(test)
    model = load_model('model/COVIDMD.h5')
    predict = model.predict_classes(test)

    for i in range(len(test)):
        result = (name[i] + " : , Predict : " + str(categories[predict[i]]))

    return result


if __name__ == "__main__":
    main()
