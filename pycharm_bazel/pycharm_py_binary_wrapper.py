import contextlib
import runpy


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

    sandbox_path_to_current_file = sys.argv[0]
    real_script = sys.argv[1]
    updated_args = [real_script, *sys.argv[2:]]


    if os.environ.get("PYCHARM_HOSTED"):
        i = sandbox_path_to_current_file.rfind('_main')
        sandbox_path_root = sandbox_path_to_current_file[: i + len('_main')]

        with new_cd(sandbox_path_root): # change the working directory to the sandbox root
            sys.argv = updated_args
            runpy.run_path(real_script, run_name="__main__")
    else:
        # Normal case when running a bazel test from the cli "bazel run ..."
        runpy.run_path(real_script, run_name="__main__")
