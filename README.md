# flask_restful_api

A simple RESTful API built with Python Flask and SQLAlchemy to easily interact with a SQLite3 database.

## Installation

In order to generate your personal database, from inside the project folder run through the terminal this command:

```
$ python
```

After entering python shell run:

```
from app import db

from app.models import Country, Championship

db.create_all()
```

After you run this commands you will see a new file created called database.sqlite (or whatever name you want --you can change it by modifing the app config in `/app/__init__.py`)
