from app import db, ma


class Country(db.Model):
    id_country = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Country {}>'.format(self.name)


class CountrySchema(ma.Schema):
    class Meta:
        fields = ['id_country', 'name']


class Championship(db.Model):
    id_championship = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    number_of_teams = db.Column(db.Integer, nullable=False)
    coefficent = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    id_country = db.Column(db.Integer, db.ForeignKey(
        'country.id_country'), nullable=False)
    country = db.relationship('Country')

    def __repr__(self):
        return '<Championship {}>'.format(self.name)


class ChampionshipSchema(ma.Schema):
    class Meta:
        fields = ['id_championship',
                  'name',
                  'number_of_teams',
                  'coefficent',
                  'ranking',
                  'id_country']


country_schema = CountrySchema()

championship_schema = ChampionshipSchema()
championships_schema = ChampionshipSchema(many=True)
