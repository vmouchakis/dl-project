# This is a simple application to generate captions for images.
#### Project of the Deep Learning course of the MSc in Data Science, NCSR-University of Peloponnese.

### Technologies:
    - Python
    - Virtualenv
    - Pip
    - Tensorflow
    - Keras
    - FastApi
    - Flickr8k dataset

### Here is the source code alongside the dataset and the saved files used in training: [Google Drive link](https://drive.google.com/drive/u/3/folders/1YlFUuwD4ea6z_nkZrA8xsmXH2RAkaBMZ).

To use this application please copy and paste the following commands:
```
# copy the repo locally
git clone https://github.com/vmouchakis/dl-project.git

# go to the directory of the app
cd dl-project

# create a virtual environment (called venv) to install the required python packages
virtualenv venv

# activate the virtual environment
source venv/bin/activate

# install the required python packages
pip3 install -r requirements.txt

# download `flickr8k` folder from Google Drive
```

Before running the application, the notebook `image_captioning.ipynb` should be used to generate the necessary files. Not a must, as the dataset files are already in this repo.


To run the application copy the following command
```
uvicorn app.main:app
```

The application will run on the following [link](http://localhost:8000/).

* It is necessary the folder `flickr8k` from the Google Drive to be downloaded, it contains all the images needed for training.

* Images for captioning must be in the `static/images` directory. Initially, they are inside the `flickr8k` folder in Google Drive. Images from any other source should be in `.jpg` format and saved in the `static/images` directory.

* Inside the `model` directory, there are the `checkpoint` directory storing the pretrained model, and the `dataset` directory storing the files needed for training.

* Inside the `vocab` directory there are the files that contain the dictionaries with the vocabulary.

### The directory structure of the app is (`dir-structure.txt`):
```
    dl-project
├──     app
│        ├── main.py (runs the app)
│        ├── predictor.py (captions given images)
├── dir-structure.txt
├──     flickr8k 
│        ├── flickr8ktextfiles
│        ├── Flickr_TextData
│        ├── Images (contains all the available images)
├──     model
│        ├── checkpoint
│        ├── dataset
│        └── image_captioning.ipynb
├── README.md
├── requirements.txt
├──     static
│        ├── css
│        └── images
├── templates
│        └── page.html (page used from fastapi to use the app)
└── vocab
    ├── i2w.pickle
    └── w2i.pickle


```

## Also please make sure that the weights of layers actually change after you load a trained model. The proper way is to compile the model first and then call model.load - frequently people compile model after loading the weights and that reinitializes them
https://github.com/keras-team/keras/issues/8149
https://stackoverflow.com/questions/42449635/why-does-my-keras-neural-network-model-output-different-values-on-a-different-ma
