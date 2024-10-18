import pytest
import pyodbc
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

    driver = db_config['driver']
    server = db_config['server']
    database = db_config['database']
    username = db_config['username']
    password = db_config['password']
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=Yes;"

    #print connection string for debugging purposes
    print(f"Connection string to connect to the database is the following: {connection_string}")

    connection = pyodbc.connect(connection_string)
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
