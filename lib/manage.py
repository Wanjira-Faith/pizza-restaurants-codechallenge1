from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from lib import app, db

# Create a Flask-Migrate instance
migrate = Migrate(app, db)

# Create Flask-Script manager
manager = Manager(app)