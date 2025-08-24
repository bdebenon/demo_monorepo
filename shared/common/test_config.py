import pytest

from shared.common.config import ConfigPaths, Config, Environment


class TestConfig:
    # Bazel's root path is the Demo Monorepo root directory where the WORKSPACE file is located.
    default_path = 'shared/common/config_for_tests.ini'

    config_paths = ConfigPaths(
        default_path=default_path,
        local_path='',
        test_path='',
        prod_path='',
    )
    config = Config(config_paths=config_paths)

    @pytest.mark.unit
    def test_get_config_section(self):
        section_name = 'test'
        key = 'test_key'
        section = self.config.get_config_by_section(section_name=section_name)
        assert section[key] == 'test_123'

    @pytest.mark.unit
    def test_get_config_section_key(self):
        section_name = 'test'
        key = 'test_key'
        value = self.config.get_config_by_section_and_key(section_name=section_name, key=key)
        assert value == 'test_123'

    @pytest.mark.unit
    def test_environment(self):
        assert self.config.environment == Environment.DEFAULT.value
