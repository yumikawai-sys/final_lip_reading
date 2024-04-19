pip list
Package        Version
-------------- -------
blinker        1.7.0
click          8.1.7
colorama       0.4.6
DateTime       5.5
dnspython      2.6.1
Flask          3.0.2
Flask-Cors     4.0.0
itsdangerous   2.1.2
Jinja2         3.1.3
MarkupSafe     2.1.5
pip            24.0
pymongo        4.6.2
python-dotenv  1.0.1
pytz           2024.1
setuptools     65.5.0
Werkzeug       3.0.1
zope.interface 6.2

pip install numpy==1.24.1
pip install opencv-python==4.6.0.66
pip install tensorflow==2.10.1
pip install scikit-image

## Installation
1. Clone the repository.
2. Create .env file under src folder (for MongoDB)


## How to start
1. Create a virtual environment by these 2 commands. 
  'python3 -m venv env'
  'env/Sctipts/activate'
2. cd src
3. command 'python server.py' to start server
4. command 'npm run dev' to start React
5. Click 'Camera' to start a video and click 'Recording' to start recording
6. Click 'Stop' to stop recording
5. Click 'Get' button to see the transcription history in console
6. Click 'Transcipt' button to get the prediction of the video

## Please note:
 Face detection, Lip area detection are in progress.

