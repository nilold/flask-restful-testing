# Flask Restful App Tests
[![Build Status](https://travis-ci.org/nilold/flask-restful-testing.svg?branch=master)](https://travis-ci.org/nilold/flask-restful-testing)

## Examples of Flask (and Python) tests

This project is a very simple flask app with REST endpoints and a basic HTML template.
It is built with Flask, Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy.


It contains, however, several tests of the kind:
- Unit
- Integration
- System
- Acceptance (BDD)
- Postman - Newman (kind of a Acceptance for REST endpoints)

The unit, integration and system tests are implemented using the builtin package **unittest**.

## Tests

### Unit, Integration and System tests
These tests will test the unit functions, endpoints CRUDs and database CRUDs  
They can be run with the pytest runner
```bash
python -m pytest tests/
```
There is also a .travis.yml configuration file, so it will run on [Travis CI](https://travis-ci.org) if you integrate the repo there.

### Acceptance tests
These tests are used for [BDD](https://behave.readthedocs.io/en/latest/philosophy.html) and will test how the webpage 
served by flask behaves in a very high level ("When I click this button, then this page opens").  
They can be run with [beahve](https://pypi.org/project/behave/) (You will also need [selenium](https://pypi.org/project/selenium/)) 
```bash
behave tests/acceptance
```

### Postman - Newman
These tests are used to test the RESTful endpoints in a high level. They can be seen as a "REST BDD". They were made 
using the [Postman](https://www.postman.com) interface. This short [video](https://youtu.be/pi9MxX0HSHU) shows how to do it.
There are ywo ways of running them:
- Importing both the [collections](tests/flask-app-test-export.postman_collection.json) and 
the [environment](tests/flask-app-test.postman_environment.json) files into Postman, the running using Postman Runner.
- Using [newman](https://learning.postman.com/docs/postman/collection-runs/command-line-integration-with-newman/), a Postman CLI runner.
To do so, install using npm (````npm install -g newman````), run the app (```python app.py```) and run newman:
````bash
newman run <collection_file.json> -e <environment_file.json>
````

If you are using Pycharm, you can make these configurations so you run everything from inside it.

Please contribute with any comments, issues notification or pull requests!