# Bazel's root path is the monorepo root directory where the MODULE.bazel file is located.
from shared.common.config import ConfigPaths, Config

configs_for_testing_in_shared_folder = 'shared/common/config_for_tests.ini'
config_paths = ConfigPaths(
    default_path=configs_for_testing_in_shared_folder,
    local_path=configs_for_testing_in_shared_folder,
    test_path=configs_for_testing_in_shared_folder,
    prod_path=configs_for_testing_in_shared_folder,
)
config = Config(config_paths=config_paths)
