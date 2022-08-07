# Person Alarm

Person alarm detect is a API service for detecting distance between the detected person and danger area you chose. It is written with python and django. Persona alarm uses yolov3 algorithm for recognizing persons in image. And it also use opencv-python for calculating distance of recognized persons from danger area that given.


## Running the app and the telegram bot

* Clone the repository
* Create ```settings_local.py``` inside persona_alarm directory
  > just rename the person_alarm/settings_local.copy.py as person_alarm/settings_local.py
  and replace neccessary variables with your own.
* Migrate db ```python maange.py migrate```
* Run the app: ```python manage.py runserver```
  > If you want to serve the app locally and networking will be done in same host, you should run the app like: ```python manage.py runserver 0.0.0.0:8000``` 
* Create SiteSettings and telegram data on admin
  * Firstly, you should create an admin user with ```python manage.py createsuperuser```
  * After that go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and create Sitesettings object
* Start the telegram bot for listening users commands: ```python manage.py startbot```
