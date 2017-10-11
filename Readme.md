## Installation

```bash
$ mkdir projects
$ cd projects
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ pip install Django
$ git clone https://gitlab.com/shamim4063/djangorest.git
$ cd djangorest
$ pip install djangorestframework
$ python3 manage.py runserver

```

## Run 
* localhost:8000/admin too see admin panel
* localhost:8000/playerlist   to see player list
* localhost:8000/playerlist/1 to see detail of palyer 1
* localhost:8000/districtlist to see districtlist