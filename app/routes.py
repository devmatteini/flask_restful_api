from flask import jsonify
from app import app
from app.models import Championship, championship_schema, championships_schema


@app.route('/api/championships', methods=['GET'])
def get_championships():
    all_championships = Championship.query.all()
    result = championships_schema.dump(all_championships)

    return jsonify(result)


@app.route('/api/championship/<int:id>', methods=['GET'])
def get_championship(id):
    championship = Championship.query.filter_by(id_championship=id).first()
    return championship_schema.jsonify(championship)
