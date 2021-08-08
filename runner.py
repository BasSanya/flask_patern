import os
from app import app, db
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
