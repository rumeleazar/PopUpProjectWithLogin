#!/bin/bash


source venv/Scripts/activate
pip install -r requirements.txt

python database.py
python app.py
