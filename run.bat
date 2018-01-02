@ECHO OFF
CALL activate tensorflow


python camera.py ALL pre-trained/20170512-110547.pb classifier.pkl --interval=1 --minsize=80


PAUSE
