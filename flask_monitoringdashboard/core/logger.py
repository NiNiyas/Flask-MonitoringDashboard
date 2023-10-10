import json
import os
import sys

from loguru import logger

LOG_FORMAT = "<magenta>{time:YYYY-MM-DD HH:mm:ss Z}</magenta> | <green>{name}</green> | <red>{level}</red> | <cyan>{message}</cyan>"
logger.add(sys.stderr, level="INFO")
logger.remove()
logger.add(
    sys.stderr,
    level="INFO",
    colorize=True,
    format=LOG_FORMAT,
    backtrace=True,
)

with open(f"{os.path.dirname(os.path.dirname(__file__))}/constants.json", "r") as f:
    constants = json.load(f)

logging = logger.patch(lambda record: record.update(name=f"Flask-MonitoringDashboard :: v{constants["version"]}"))


def log(string):
    """
    Only print output if this is specified in the configuration
    :param string: string to be printed
    """
    from flask_monitoringdashboard import config

    if config.enable_logging:
        logging.info(string)
