# flask_restful_api

A simple RESTful API built with Python Flask and SQLAlchemy to easily interact with a SQLite3 database.

## Installation

In order to generate your personal database, from inside the project folder run through the terminal this command:

```bash
$ python
```

After entering python shell run:

```python
from app import db

from app.models import Country, Championship

db.create_all()
```

After you run this commands you will see a new file created called database.sqlite (or whatever name you want --you can change it by modifing the app config in `/app/__init__.py`)

## API Endpoints

```
GET /api/championships
```

List of all the champsionships.

Response:

```json
[
    {
        "coefficent":58010,
        "id_championship":1,
        "id_country":1,
        "name":"Serie A",
        "number_of_teams":20,
        "ranking":4
    },
    {
        "coefficent":74176,
        "id_championship":2,
        "id_country":2,
        "name":"Premier League",
        "number_of_teams":20,
        "ranking":2
    },
    ...
]
```

---

```
GET /api/championship/<int:id>
```

Championship corresponding to the `id` provided

Response:

```json
{
	"coefficent": 85640,
	"id_championship": 4,
	"id_country": 4,
	"name": "La Liga",
	"number_of_teams": 20,
	"ranking": 1
}
```
