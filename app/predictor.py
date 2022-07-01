import numpy as np
from tensorflow.keras.applications import ResNet50\
from tensorflow.keras.models import load_model


MAX_LEN = 40

class Predictor():

    

    img = "./Images/1453366750_6e8cf601bf.jpg"

    test_img = get_encoding(resnet, img)

    def predict_captions(image):
        start_word = ["<start>"]
        while True:
            par_caps = [word_2_indices[i] for i in start_word]
            par_caps = sequence.pad_sequences([par_caps], maxlen=MAX_LEN, padding='post')
            preds = model.predict([np.array([image]), np.array(par_caps)])
            word_pred = indices_2_word[np.argmax(preds[0])]
            start_word.append(word_pred)
            
            if word_pred == "<end>" or len(start_word) > MAX_LEN:
                break
                
        return ' '.join(start_word[1:-1])

    Argmax_Search = predict_captions(test_img)

    def predict(self, image):

        # load the model for the captioning prediction
        model = load_model("./model/model.h5")

        # load ResNet model (pretrained)
        resnet = ResNet50(include_top=False, weights="imagenet", nput_shape=(224,224,3), pooling="avg")
        
        # function to preprocess image (size)
        def preprocessing(img_path):
            im = image.load_img(img_path, target_size=(224,224,3))
            im = image.img_to_array(im)
            im = np.expand_dims(im, axis=0)
            return im

        # function to get image encoding
        def get_encoding(model, img):
            image = preprocessing(img)
            pred = model.predict(image).reshape(2048)
            return pred

