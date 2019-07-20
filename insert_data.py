import json
from app import db
from app.models import Country, Championship

# RUN THIS FILE AFTER CREATING THE DATABASE FILE

source = json.load(open('source.json', 'r'))
print('Data loaded from <source.json>\nAdding to database...')


def add_country(country):
    new_country = Country(name=country)
    db.session.add(new_country)
    return new_country


countries = [add_country(country) for country in source['countries']]
db.session.commit()


def add_championship(championship, country):
    new_championship = Championship(name=championship['name'],
                                    number_of_teams=championship['number_of_teams'],
                                    coefficent=championship['coefficent'],
                                    ranking=championship['ranking'],
                                    country=country)
    db.session.add(new_championship)


for i, championship in enumerate(source['championships']):
    add_championship(championship, countries[i])

db.session.commit()

print('Data loaded into the database correctly')
