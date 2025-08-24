load("@rules_python//python:py_binary.bzl", "py_binary")
load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")
load("@pip_example_fast_api//:requirements.bzl", "requirement")

py_library(
    name = "service",
    srcs = [
        "__init__.py",
        "app.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        requirement("uvicorn"),
        requirement("fastapi"),
        "//services/example_fast_api/src/common",
        "//services/example_fast_api/src/service/patients",
        "//shared/common",
    ],
)

py_binary(
    name = "app",
    srcs = [
        ":service",
    ],
    main = "app.py",
    deps = [
        ":service",
    ],
)

test_suite(
    name = "test_unit",
    tests = [
        "//services/example_fast_api/src/service/patients:test_unit",
    ],
)
