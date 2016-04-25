#!/bin/bash
pip install -r requirements.txt
python manage.py celeryd -B &
python manage.py runserver

