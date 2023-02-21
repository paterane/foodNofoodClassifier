from tensorflow.keras.models import load_model
from PIL import Image
import joblib
import numpy as np

class Classifier:
    __model = load_model('resnet_model/')
    __classes = joblib.load('output_classes.save')
    def getImageData(image):
        '''
        Return: np.array of image data
        '''
        im = Image.open(image, 'r')
        if ''.join(im.getbands()) != 'RGB':
            im = im.convert('RGB').resize((180,180))
        else:
            im = im.resize((180,180))
        im_data = np.array(im.getdata()).reshape(1,180,180,3)
        return im_data
    def showImage(image):
        '''
        It will show an image of the file specified
        '''
        im = Image.open(image, 'r').resize((180,180))
        im.show()
    def IsFood(image_data):
        '''
        Return: 'food' or 'non_food' out of classes
        '''
        predict = Classifier.__model.predict(image_data)
        classes = Classifier.__classes[np.argmax(predict.reshape(-1,))]
        return classes