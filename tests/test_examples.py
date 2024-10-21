import pytest
from tools.connector import *
from tools.checkers import (check_for_completeness, check_maximum_length,
    check_allowed_values, check_uniqueness, check_regex_patterns,
    check_positive_values)

@pytest.mark.hr
@pytest.mark.countries
def test_country_name_completeness(fetch_data):
    """
    Test to verify that all entries in the country_name column of the [hr].[countries]
    table are complete with no null or empty values.
    """
    query = "SELECT country_name FROM [hr].[countries]"
    cities = [record[0] for record in fetch_data(query)]
    assert check_for_completeness(cities), "City completeness check failed."

@pytest.mark.hr
@pytest.mark.countries
def test_country_id_max_length(fetch_data):
    """
    Test to verify that every country_id from the [hr].[countries] table does not exceed
    a maximum length of 2 characters.
    """
    max_length = 2
    query = "SELECT country_id FROM [hr].[countries]"
    country_ids = [record[0] for record in fetch_data(query)]
    assert check_maximum_length(country_ids, max_length), f"Country ID max length of {max_length} characters is exceeded."


@pytest.mark.hr
@pytest.mark.regions
def test_country_ids_uniqueness(fetch_data):
    """
    Test  to verify that each country_id from the [hr].[countries] table is unique,
    there no duplicate IDs.
    """
    query = "SELECT country_id FROM [hr].[countries]"
    countries_ids = [record[0] for record in fetch_data(query)]
    assert check_uniqueness(countries_ids), "Country ID uniqueness check failed."


@pytest.mark.hr
@pytest.mark.countries
def test_country_id_completeness(fetch_data):
    """
    Test to verify that all entries in the country_id column of the [hr].[countries]
    table are complete with no null or empty values.
    """
    query = "SELECT country_id FROM [hr].[countries]"
    country_ids = [record[0] for record in fetch_data(query)]
    assert check_for_completeness(country_ids), "Country IDs completeness check failed."


@pytest.mark.hr
@pytest.mark.regions
def test_regions_name_allowed_values(fetch_data):
    """
    Test to verify all region_name entries from the [hr].[regions] table are limited to specific allowed
    values, verifying the entry against a predefined list of acceptable region names.
    """
    allowed_values = ["Europe", "Americas", "Asia", "Middle East and Africa"]
    query = "SELECT region_name FROM [hr].[regions]"
    region_names = [record[0] for record in fetch_data(query)]
    assert check_allowed_values(region_names, allowed_values), "Region name allowed values check failed."


@pytest.mark.hr
@pytest.mark.regions
def test_region_ids_uniqueness(fetch_data):
    """
    Test  to verify that each region_id from the [hr].[regions] table is unique,
    there no duplicate IDs.
    """
    query = "SELECT region_id FROM [hr].[regions]"
    region_ids = [record[0] for record in fetch_data(query)]
    assert check_uniqueness(region_ids), "Region ID uniqueness check failed."


@pytest.mark.hr
@pytest.mark.employees
def test_employee_email_format(fetch_data):
    """
    Test to verify that all employee emails in [hr].[employees]
    table match the specified regular expression pattern.
    """
    pattern = r'^[A-Za-z0-9._%+-]+@sqltutorial\.org$'
    query = "SELECT email FROM [hr].[employees]"
    emails = [record[0] for record in fetch_data(query)]
    assert check_regex_patterns(emails, pattern), f"Email format check failed for pattern {pattern}."


@pytest.mark.hr
@pytest.mark.employees
def test_employee_salaries_positive(fetch_data):
    """
    Test to verify that all employee salaries values in [hr].[employees]
    table are positive.
    """
    query = "SELECT salary FROM [hr].[employees]"
    salaries = [record[0] for record in fetch_data(query)]
    assert check_positive_values(salaries), "All salary values should be greater than 0."
