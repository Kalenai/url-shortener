import click
import os
import unittest
from app import create_app, db
from app.models import UrlLink


app = create_app(os.getenv('APP_SETTINGS'))


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, UrlLink=UrlLink)


@app.cli.command()
def recreate_db():
    click.echo('Recreating database...')
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo('Finished reacreating database.')


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
