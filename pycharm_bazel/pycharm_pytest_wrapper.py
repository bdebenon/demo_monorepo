import contextlib


@contextlib.contextmanager
def new_cd(x):
    d = os.getcwd()

    # This could raise an exception, but it's probably
    # best to let it propagate and let the caller
    # deal with it, since they requested x
    os.chdir(x)

    try:
        yield

    finally:
        os.chdir(d)

if __name__ == "__main__":
    import os
    import sys

    import pytest

    if os.environ.get("PYCHARM_HOSTED"):
        # sys.argv[0] this has the location of pytest_test.py within the sandbox.
        sandbox_path_to_current_file = sys.argv[0]
        i = sandbox_path_to_current_file.rfind('_main')
        sandbox_path_root = sandbox_path_to_current_file[: i + len('_main')]

        with new_cd(sandbox_path_root): # change the working directory to the sandbox root
            sys.exit(pytest.main(sys.argv[1:]))
    else:
        # Normal case when running a bazel test from the cli "bazel test ..."
        sys.exit(pytest.main(sys.argv[1:]))