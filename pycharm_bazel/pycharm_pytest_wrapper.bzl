load("@rules_python//python:defs.bzl", "py_test")

def pycharm_pytest_wrapper(name, srcs, data = [], deps = [], args = [], **kwargs):
    py_test(
        name = name,
        srcs = ["//pycharm_bazel:pycharm_pytest_wrapper.py"] + srcs,
        main = "pycharm_pytest_wrapper.py",
        args = args,
        deps = deps,
        data = data,
        **kwargs
    )
