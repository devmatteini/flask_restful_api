from app import app


@app.route('/api/championships', methods=['GET'])
def get_championships():
    pass


@app.route('/api/championship/<int:id>', methods=['GET'])
def get_championship(id):
    pass
