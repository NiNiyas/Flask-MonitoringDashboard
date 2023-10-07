"""Contains custom commands for the Flask-MonitoringDashboard
For a list of all commands, open a terminal and type:

>>> flask fmd --help
"""

import click
from flask.cli import with_appcontext

from flask_monitoringdashboard import log


@click.group()
def fmd():
    pass


@fmd.command()
@with_appcontext
def init_db():
    # Importing the database package is enough
    import flask_monitoringdashboard.database

    log("Flask-MonitoringDashboard database has been created")
