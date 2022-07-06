# This is a simple application to generate captions for images.
#### Project of the Deep Learning course of the MSc in Data Science, NCSR-University of Peloponnese 

- [Google Drive link](https://drive.google.com/drive/u/3/folders/1YlFUuwD4ea6z_nkZrA8xsmXH2RAkaBMZ)

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
```

Before running the application, the notebook `image_captioning.ipynb` should be used to generate the necessary files.

To run the application copy the following command
```
uvicorn app.main:app
```

The application will run on the following [link](http://localhost:8000/).

* Images must be in the `static/images` directory

* Inside the `model` directory, there are the `checkpoint` directory storing the pretarained model, and the `dataset` directory storing the files needed for training.

* Inside the `vocab` directory there are the the files the contain the dictionaries with the vocabulary.