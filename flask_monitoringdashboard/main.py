"""This file can be executed for developing purposes.
To run use:

>>> python main.py

Note: This is not used when the flask_monitoring_dashboard
is attached to your flask application.
"""
from random import random

from flask import Flask, redirect, url_for

import flask_monitoringdashboard as dashboard

app = Flask(__name__)


dashboard.config.version = "3.2"
dashboard.config.group_by = "2"
dashboard.config.database_name = "sqlite:///data.db"


def on_the_minute():
    return int(random() * 100 // 10)


minute_schedule = {"second": 00}
dashboard.add_graph("On Half Minute", on_the_minute, "cron", **minute_schedule)


def every_ten_seconds():
    return int(random() * 100 // 10)


every_ten_seconds_schedule = {"seconds": 10}
dashboard.add_graph("Every 10 Seconds", every_ten_seconds, "interval", **every_ten_seconds_schedule)


@app.route("/")
def to_dashboard():
    return redirect(url_for(dashboard.config.blueprint_name + ".login"))


if __name__ == "__main__":
    dashboard.bind(app)
    app.run()
