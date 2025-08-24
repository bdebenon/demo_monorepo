load("@pip_example_fast_api//:requirements.bzl", "requirement")

py_library(
    name = "patients",
    srcs = [
        "__init__.py",
        "patients_router.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        requirement("fastapi"),
        requirement("dependency-injector"),
        "//services/example_fast_api/src/domain/patients",
        "//services/example_fast_api/src/service/dependency_injection",
        "//services/example_fast_api/src/service/patients/use_cases",
    ],
)

load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")

pycharm_pytest_wrapper(
    name = "test_unit",
    srcs = [
        "test_patients_router.py",
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
        requirement("pytest-asyncio"),
        requirement("dependency-injector"),
        requirement("httpx"),
        requirement("fastapi"),
        ":patients",
        "//services/example_fast_api/src/domain/patients",
        "//services/example_fast_api/src/domain/patients/definitions:fakers",
        "//services/example_fast_api/src/infra/patients",
        "//services/example_fast_api/src/service",
    ],
)
