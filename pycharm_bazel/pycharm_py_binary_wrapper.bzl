load("@rules_python//python:defs.bzl", "py_binary")

def pycharm_py_binary_wrapper(
        name,
        srcs,
        data = [],
        deps = [],
        args = [],
        main_src = None,
        **kwargs):
    if not srcs:
        fail("pycharm_py_binary_wrapper: 'srcs' must contain at least one file")

    if main_src == None:
        main_src = srcs[0]  # assume first src is the real entry-point

    py_binary(
        name = name,
        srcs = ["//pycharm_bazel:pycharm_py_binary_wrapper.py"] + srcs,
        main = "pycharm_py_binary_wrapper.py",
        args = ["$(execpath %s)" % main_src] + args,
        deps = deps,
        data = data,
        **kwargs
    )
