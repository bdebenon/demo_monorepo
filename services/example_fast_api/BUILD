# We do this to satisfy IntelliJ - it thinks README.md is a build target and fails to sync without this
filegroup(
    name = "ignore_targets",
    srcs = [
        "Dockerfile",
        "Makefile",
        "README.md",
        "requirements.txt",
        "requirements_test.txt",
    ],
    visibility = ["//visibility:public"],
)

load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements_combined.in",
    requirements_txt = "requirements_lock.txt",
)

py_library(
    name = "example_fast_api",
    srcs = [
        "__init__.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//services/example_fast_api/src",
    ],
)

test_suite(
    name = "test_unit",
    tests = [
        "//services/example_fast_api/src/common:test_unit",
        "//services/example_fast_api/src/domain:test_unit",
        "//services/example_fast_api/src/infra:test_unit",
        "//services/example_fast_api/src/service:test_unit",
    ],
)

test_suite(
    name = "test_integration",
    tests = [
        "//services/example_fast_api/src/infra:test_integration",
    ],
)

test_suite(
    name = "test_all",
    tests = [
        ":test_integration",
        ":test_unit",
    ],
)
