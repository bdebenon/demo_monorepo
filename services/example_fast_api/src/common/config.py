from shared.common.config import ConfigPaths, Config

# Bazel's root path is the Demo Monorepo root directory where the WORKSPACE file is located.
local_path = 'services/example_fast_api/configs/local.ini'
test_path = 'services/example_fast_api/configs/test.ini'
prod_path = 'services/example_fast_api/configs/prod.ini'

config_paths = ConfigPaths(
    default_path=local_path,
    local_path=local_path,
    test_path=test_path,
    prod_path=prod_path,
)
config = Config(config_paths=config_paths)
