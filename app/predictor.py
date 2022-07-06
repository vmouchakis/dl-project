from jinja2 import ModuleLoader
import numpy as np
import os
from IPython.display import Image, display
import pickle
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from keras.backend import manual_variable_initialization 
manual_variable_initialization(True)
from keras.preprocessing import image
from keras.models import model_from_json
# from keras.preprocessing.sequence import pad_sequences
from keras_preprocessing.sequence import pad_sequences
from fastapi.responses import FileResponse


MAX_LEN = 40

with open('./vocab/w2i.pickle', 'rb') as handle:
    word_2_indices = pickle.load(handle)

with open('./vocab/i2w.pickle', 'rb') as handle:
    indices_2_word = pickle.load(handle)

class Predictor():

    def predict(self, image_name):
        

        # load the model for the captioning prediction

        # 1st way:
        json_file = open('./model/checkpoint/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights("./model/checkpoint/model.h5")
        print("Loaded model from disk")

        # 2nd way:
        # model = load_weights("./model/checkpoint/model_weights.h5")
        # print("Model loaded.")

        model.compile(loss='categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])

        # load ResNet model (pretrained)
        resnet = ResNet50(include_top=False, weights="imagenet", input_shape=(224,224,3), pooling="avg")
        
        # function to preprocess image (size)
        def preprocessing(img_path):
            im = load_img(img_path, target_size=(224,224,3))
            # im = image.load_img(img_path, target_size=(224,224,3))
            im = img_to_array(im)
            # im = image.img_to_array(im)
            im = np.expand_dims(im, axis=0)
            return im

        # function to get image encoding
        def get_encoding(model, img):
            image = preprocessing(img)
            pred = model.predict(image).reshape(2048)
            return pred


        # test with a specific image
        # img = "./flickr8k/Images/1453366750_6e8cf601bf.jpg"
        img = "./flickr8k/Images/" + image_name
        test_img = get_encoding(resnet, img)

        # get prediction
        def predict_captions(image):
            start_word = ["<start>"]
            while True:
                par_caps = [word_2_indices[i] for i in start_word]
                par_caps = pad_sequences([par_caps], maxlen=MAX_LEN, padding='post')
                preds = model.predict([np.array([image]), np.array(par_caps)])
                word_pred = indices_2_word[np.argmax(preds[0])]
                start_word.append(word_pred)
                
                if word_pred == "<end>" or len(start_word) > MAX_LEN:
                    break
                    
            return ' '.join(start_word[1:-1])

        caption = predict_captions(test_img)
        caption = caption.replace("laden", "")
        caption = caption.replace("mulch", "")
        caption = caption.replace("on-lookers", "")
        caption = caption.replace("speaks", "")
        caption = caption.replace("like", "")

        z = Image(filename=img)
        display(z)

        print(caption)
        print(image_name)

        
        return caption, image_name