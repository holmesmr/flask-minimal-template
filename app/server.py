from flask import Flask, jsonify


def create_app():
    # create and configure the app
    app = Flask(__name__)

    # Add routes to application.
    routes(app)

    return app


def routes(app):
    @app.route("/")
    def hello_world():
        return jsonify({"content": "Hello, world!"})
