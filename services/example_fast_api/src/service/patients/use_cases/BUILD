load("@pip_example_fast_api//:requirements.bzl", "requirement")

py_library(
    name = "use_cases",
    srcs = [
        "__init__.py",
        "get_patients_use_case.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//services/example_fast_api/src/infra/patients",
    ],
)

load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")

pycharm_pytest_wrapper(
    name = "test_unit",
    srcs = [
        "test_get_patients_use_case.py",
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
        ":use_cases",
        "//services/example_fast_api/src/domain/patients/definitions:fakers"
    ],
)
