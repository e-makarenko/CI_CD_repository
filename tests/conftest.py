import pytest

def pytest_configure(config):
    """
    Configures pytest custom markers.
    """
    config.addinivalue_line(
        "markers", "hr: mark hr schema."
    )
    config.addinivalue_line(
        "markers", "employees: mark employees table."
    )
    config.addinivalue_line(
        "markers", "countries: mark countries table."
    )
    config.addinivalue_line(
        "markers", "regions: mark regions table."
    )


def pytest_metadata(metadata):
    """
    Modifies metadata configurations for pytest.
    """
    metadata['Project Name'] = 'Pytest Framework Project'
    metadata['Environment'] = 'Development'