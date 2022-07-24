# untitled_nlidb
Final Year Project NLIDB

## INSTALLATION
Tested on debian11, Arch and wsl(ubuntu)

## Requirements
- python 3.9.2
- python-venv 3.9.2

## Backend
- Navigate to /backend
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- `python3 -m nltk.downloader -d env/nltk_data stopwords punkt'`
- `python3 manage.py runserver`
- `deactivate` to exit virtual environment

## Frontend
- Navigate to /frontend
- `npm install`
- `expo start`
