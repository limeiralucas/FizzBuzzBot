from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from fizzbuzz_core.data.models import db
from fizzbuzz_core import create_app
from app import config

app = create_app(config)
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
