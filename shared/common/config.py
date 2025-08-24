import configparser
import os.path
from enum import Enum
from os import getcwd

ENV_ENVIRONMENT_VARIABLE = 'ENVIRONMENT'


class Environment(Enum):
    DEFAULT = 'default'
    LOCAL = 'local'
    TEST = 'test'
    PROD = 'prod'


class ConfigPaths:
    def __init__(self, default_path: str, local_path: str, test_path: str, prod_path: str):
        self._default_path = default_path
        self._local_path = local_path
        self._test_path = test_path
        self._prod_path = prod_path

    @property
    def default_path(self) -> str:
        return self._default_path

    @property
    def local_path(self) -> str:
        return self._local_path

    @property
    def test_path(self) -> str:
        return self._test_path

    @property
    def prod_path(self) -> str:
        return self._prod_path


class Config:
    def __init__(self, config_paths: ConfigPaths):
        self._config = configparser.ConfigParser()
        self._environment = os.getenv(ENV_ENVIRONMENT_VARIABLE, Environment.DEFAULT.value)
        if self._environment == Environment.DEFAULT.value:
            self._config_path = config_paths.default_path
        elif self._environment == Environment.LOCAL.value:
            self._config_path = config_paths.local_path
        elif self._environment == Environment.TEST.value:
            self._config_path = config_paths.test_path
        elif self._environment == Environment.PROD.value:
            self._config_path = config_paths.prod_path
        else:
            raise Exception(f'Invalid environment found: {self._environment}')
        self._config.read(self._config_path)

    def get_config_by_section(self, section_name: str) -> configparser.SectionProxy:
        try:
            return self._config[section_name]
        except KeyError:
            raise KeyError(f'Section_name "{section_name}" does not exist in the config file. '
                           f'Ensure your working directory is set properly. '
                           f'Current working directory is "{getcwd()}". '
                           f'Target config file is "{self._config_path}". '
                           f'ENV_ENVIRONMENT_VARIABLE is: "{os.getenv(ENV_ENVIRONMENT_VARIABLE)}".')

    def get_config_by_section_and_key(self, section_name: str, key: str) -> str:
        try:
            return self._config[section_name][key]
        except KeyError as e:
            raise KeyError(f'key "{key}" does not exist in the config section "{section_name}". '
                           f'Ensure your working directory is set properly. '
                           f'Current working directory is "{getcwd()}". '
                           f'Target config file is "{self._config_path}". '
                           f'ENV_ENVIRONMENT_VARIABLE is: "{os.getenv(ENV_ENVIRONMENT_VARIABLE)}".')

    @property
    def environment(self) -> str:
        return self._environment

    @property
    def config_path(self) -> str:
        return self._config_path
