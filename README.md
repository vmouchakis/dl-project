# This is a simple application to generate captions for images.
#### Project of the Deep Learning course of the MSc in Data Science, NCSR-University of Peloponnese 

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

To run the application copy the following command
```
uvicorn app.main:app
```

The application will run on the following [link](http://localhost:8000/).