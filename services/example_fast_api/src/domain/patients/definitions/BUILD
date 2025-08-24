load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")
load("@pip_example_fast_api//:requirements.bzl", "requirement")

py_library(
    name = "definitions",
    srcs = [
        "__init__.py",
        "models.py",
    ],
    visibility = ["//visibility:public"],
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
        ":definitions",
    ],
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
        # Mark tests as .only (Bazel excludes tests not marked with .only if at least 1 test is marked as .only)
        requirement("pytest-only"),
        ":definitions",
        ":fakers",
    ],
)
