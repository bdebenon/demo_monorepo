load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")
load("@pip_example_fast_api//:requirements.bzl", "requirement")

py_library(
    name = "patients",
    srcs = [
        "__init__.py",
        "in_memory_patients_repository.py",
        "patients_repository.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//services/example_fast_api/src/domain/patients",
    ],
)

pycharm_pytest_wrapper(
    name = "test_unit",
    srcs = [
        "test_in_memory_patients_repository.py",
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
        ":patients",
        "//services/example_fast_api/src/domain/patients/definitions:fakers",
    ],
)

