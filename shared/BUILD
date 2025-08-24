load("@rules_python//python:pip.bzl", "compile_pip_requirements")

# We do this to satisfy IntelliJ - it thinks README.md is a build target and fails to sync without this
filegroup(
    name = "readme",
    srcs = [
        "Makefile",
        "README.md",
        "requirements.txt",
        "requirements_test.txt",
    ],
    visibility = ["//visibility:public"],
)

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements_combined.in",
    requirements_txt = "requirements_lock.txt",
)

test_suite(
    name = "test_unit",
    tests = [
        "//shared/common:test_unit",
        "//shared/domain/customers/definitions:test_unit",
        "//shared/infra/customers:test_unit",
    ],
)

py_library(
    name = "shared",
    srcs = [
        "__init__.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//shared/common",
        "//shared/domain",
        "//shared/infra",
    ],
)
