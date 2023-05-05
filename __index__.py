from pathlib import Path
from database import db
from flask import Flask
from flask_cors import CORS
from exceptions import ApiError
from routes import routes

import os

app = Flask(__name__)
CORS(app, supports_credentials=True)

for route in routes:
    app.register_blueprint(route, url_prefix='/api')


@app.errorhandler(ApiError.ApiError)
def api_error(error):
    return error.message, error.status


@app.errorhandler(404)
def api_error(error):
    return 'Url not found', 404


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    with db:
        db.create_tables([])

    app.run(debug=os.environ.get('DEBUG') or False, port=os.environ.get('PORT'))
