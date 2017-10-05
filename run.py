#!flask/bin/python
from my_app.app import app, db
from my_app.config import Configuration

if __name__ == '__main__':
    app.run()
