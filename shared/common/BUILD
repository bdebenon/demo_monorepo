load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")
load("@pip_shared//:requirements.bzl", "requirement")

# We do this to satisfy IntelliJ - it thinks README.md is a build target and fails to sync without this
filegroup(
    name = "readme",
    srcs = ["README.md"],
    visibility = ["//visibility:public"],
)

filegroup(
    name = "configs",
    srcs = [
        "config_for_tests.ini",
    ],
    visibility = ["//visibility:public"],
)

py_library(
    name = "common",
    srcs = [
        "__init__.py",
        "config.py",
    ],
    visibility = ["//visibility:public"],
)


py_library(
    name = "shared_config_instance",
    srcs = [
        "shared_config_instance.py",
    ],
    data = [
        ":configs",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":common",
    ],
)

pycharm_pytest_wrapper(
    name = "test_unit",
    srcs = [
        "test_config.py",
    ],
    args = [
        "-m",
        "unit",
    ],
    data = [
        ":configs",
        "//:pytest_ini",
    ],
    deps = [
        "//shared/common",
        requirement("pytest"),
    ],
)
