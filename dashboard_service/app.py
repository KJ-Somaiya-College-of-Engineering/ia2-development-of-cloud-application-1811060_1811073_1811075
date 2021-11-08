from flask import Flask, make_response
from flask_cors import CORS

from tracer.blueprints.auth import app as auth_blueprint
from tracer.blueprints.url import app as url_blueprint
from tracer.blueprints.tpoints import app as tpoints_blueprint

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

app.register_blueprint(auth_blueprint)
app.register_blueprint(url_blueprint)
app.register_blueprint(tpoints_blueprint)

@app.route('/')
def home():
    return make_response('<center><h2>APIs for Tracer hosted here.</h2></center>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')