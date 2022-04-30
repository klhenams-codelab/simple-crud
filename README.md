# simple-crud

Requirements
---

* Python `3.9+`
* Postgresql `2.9+`
* Django `3.2+`


> ***Note***: Use a virtual environment or container for project isolation 

## Depednency Installations
---
## 1. Set up configuration file

Locate `src/.env.dist`

Rename `.env.dist` to `.env`

# Running application
Run this command to install dependencies

`pip install -r ./appliances/requirements.txt `

To set up the database run the following commands sequentially

`python manage.py migrate`

`python manage.py loaddata -i database/seed/dump.json`

Run command to start application

`python manage.py runserver`
