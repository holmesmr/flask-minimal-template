Flask Minimal Template
======================

A simple Flask project with pytest and requests preinstalled.

The main code for the Flask app exists in `app/server.py`.

## Versions

Flask: 2.1.1
pytest: 7.1.1
requests: 2.27.1

## Requirements

* Python 3.7 or newer (as required by Flask)
* pip

## Installation instructions

1. Create a new virtualenv in the project.
2. Install the dependencies using `pip install -r requirements.txt`

## Running instructions

### Server

The server can be run from within the virtualenv by either running
`FLASK_APP=app flask run` or `python -m app`.

### Tests

Tests can be run using `pytest` from within the virtualenv.
