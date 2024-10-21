import os
import yaml
import pathlib

def get_yaml_config(config_file: str) -> dict:
    """
    Reads yaml file and returns dictionary.
    :param config_file: file path
    :return: dictionary
    """
    directory = pathlib.Path(__file__).parent.resolve()
    config_file_path = os.path.join(directory, config_file)
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file.read())
        return config
