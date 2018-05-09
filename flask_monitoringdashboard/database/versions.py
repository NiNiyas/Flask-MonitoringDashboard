from sqlalchemy import func, asc

from flask_monitoringdashboard.database import FunctionCall


def get_date_first_request(db_session, version=None):
    """
    :param db_session: session for the database
    :param version: optional: first date when this version is requested
    :return: a datetime object with the value of when the first request is made
    """
    result = db_session.query(FunctionCall.time). \
        filter((FunctionCall.version == version) | (version is None)).first()
    if result:
        return result[0]
    return None


def get_versions(db_session, end=None):
    """
    Returns a list of length 'limit' with the versions that are used in the application
    :param db_session: session for the database
    :param end: the versions that are used in a specific endpoint
    :return: a list with the versions (as a string)
    """
    result = db_session.query(FunctionCall). \
        filter((FunctionCall.endpoint == end) | (end is None)). \
        order_by(asc(FunctionCall.time)).all()
    return list(set([row.version for row in result]))


def get_first_requests(db_session):
    """
    Returns a list with all versions and when they're first used
    :param db_session: session for the database
    :return:
    """
    return db_session.query(FunctionCall.version, func.min(FunctionCall.time)).\
        group_by(FunctionCall.version).all()
