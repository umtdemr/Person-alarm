# Person Alarm

Person alarm detect is a API service for detecting distance between the detected person and danger area you chose. It is written with python and django. Persona alarm uses yolov3 algorithm for recognizing persons in image. And it also use opencv-python for calculating distance of recognized persons from danger area that given.


## Running app and Bot

* Clone the repository
* Create ```settings_local.py``` inside persona_alarm directory
* Migrate db ```python maange.py migrate```
* Create settings and telegram data on admin
* Run the app: ```python manage.py runserver```
  > If you want to serve the app locally and networking will be done in same host, you should run the app like: ```python manage.py runserver 0.0.0.0:8000``` 
* Start the bot for listening commands: ```python manage.py startbot```

## TODO

- [x] Process captured image directly 
- [x] Increase quality of captured image
  > I can't do anything about it with code. The cold time of camera effects the quality directly
- [x] Delete percent of confidence from determined stuff 
- [x] Set on off control with telegram
