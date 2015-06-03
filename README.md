# google_pred_api_test
Handwritten Digits Recognition Using Google Prediction API ?

This project is just ... for fun. 
The image used in this project was acquired from OpenCV sample folder (opencv/samples/python2/data/digits.png), thus it's not included here.


Dependencies:
Python 2.7
Google App Engine
Google API Python Client
OpenCV
NumPy

How to run:
1. 'prepare_data.py'
	This will generate training data in cvs format and testing data in txt format. 
	Training data contains 2500 digits (0 - 9), 250 for each. 
	There are 10 txt files for testing purposes, each contains one sample.

2. 'train.py'
	Before training, create your client ID as a installed application type, and place your 
	'client_secrets.json' file in the same folder.
	The prediction API will create a classification model. 

3. 'predict.py'
	Choose any txt file in 'test_data' folder and make prediction. The result is shown in both bar and pie charts.
	
References:
http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_ml/py_knn/py_knn_opencv/py_knn_opencv.html#knn-opencv
https://developers.google.com/api-client-library/python/auth/installed-app
http://cloudacademy.com/blog/google-prediction-api/
https://cloud.google.com/prediction/docs/developer-guide
