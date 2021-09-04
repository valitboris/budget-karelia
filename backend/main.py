from flask import Flask
from flask import render_template
from rotes import route

def create_flask_app():
    app = Flask(__name__)
    route(app)
    app.config['WTF_CSRF_ENABLED'] = False
    return app

if __name__ == '__main__':
    create_flask_app().run().host='0.0.0.0'
