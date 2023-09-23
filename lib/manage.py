from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

app = create_app()

# Create a Flask-Migrate instance
migrate = Migrate(app, db)

# Create Flask-Script manager
manager = Manager(app)

# Add Flask-Migrate commands to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()