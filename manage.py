import os
import unittest

from flask_migrate import Migrate
from flask_cli import FlaskGroup

from app.main import create_app, db
from app.main.model import company

from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

cli = FlaskGroup(app)

migrate = Migrate()
migrate.init_app(app, db)


@cli.command('run')
def run():
    app.run()

@cli.command('test')
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()