import pytest
import pymssql
from config.configs import get_yaml_config


@pytest.fixture(scope="session")
def db_connection():
    """
    Fixture that retrieves connection parameters from database config,
    opens and closes database connection for a test session.
    """
    config_name = 'db_connection_config.yaml'
    db_config = get_yaml_config(config_name)
    print(db_config)

    server = db_config['server']
    database = db_config['database']
    username = db_config['username']
    password = db_config['password']

    # Connect to the database
    connection = pymssql.connect(server=server, port='1433', user=username, password=password, database=database)
    yield connection
    connection.close()


@pytest.fixture(scope="function")
def fetch_data(db_connection):
    """
    Fixture to execute provided SQL query and return fetched data.
    """
    def fetch(query):
        cursor = db_connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    return fetch
