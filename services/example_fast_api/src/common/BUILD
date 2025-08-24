load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")
load("@pip_example_fast_api//:requirements.bzl", "requirement")

py_library(
    name = "common",
    srcs = [
        "__init__.py",
        "config.py",
    ],
    data = [
        "//services/example_fast_api/configs",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//shared/common",
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
        "//:pytest_ini",
    ],
    deps = [
        ":common",
        requirement("pytest"),
        # Mark tests as .only (Bazel excludes tests not marked with .only if at least 1 test is marked as .only)
        requirement("pytest-only"),
    ],
)
