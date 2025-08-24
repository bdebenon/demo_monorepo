load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")
load("@pip_shared//:requirements.bzl", "requirement")

py_library(
    name = "definitions",
    srcs = [
        "__init__.py",
        "models.py",
    ],
    visibility = ["//shared/domain/customers:__subpackages__"],
    deps = [
        requirement("pydantic"),
    ],
)

py_library(
    name = "fakers",
    srcs = [
        "fakers.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        requirement("faker"),
        ":definitions",
    ],
)

py_library(
    name = "constants",
    srcs = [
        "constants.py",
    ],
    visibility = ["//visibility:public"],
)

pycharm_pytest_wrapper(
    name = "test_unit",
    srcs = [
        "test_models.py",
    ],
    args = [
        "-m",
        "unit",
    ],
    data = ["//:pytest_ini"],
    deps = [
        requirement("pytest"),
        ":fakers",
    ],
)
