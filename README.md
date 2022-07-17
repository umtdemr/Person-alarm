# Person Alarm

Person alarm detect is a API service for detecting distance between the detected person and danger area you chose. It is written with python and django. Persona alarm uses yolov3 algorithm for recognizing persons in image. And it also use opencv-python for calculating distance of recognized persons from danger area that given.


## Starting app

* Clone the repository
* Create ```settings_local.py``` inside persona_alarm directory
* Migrate db ```python maange.py migrate```
* Create settings and telegram data on admin
* Run the app: ```python manage.py runserver```
* Start the bot for listening commands: ```python manage.py startbot```

## TODO

- [x] Process captured image directly 
- [x] Increase quality of captured image
  > I can't do anything about it with code. The cold time of camera effects the quality directly


