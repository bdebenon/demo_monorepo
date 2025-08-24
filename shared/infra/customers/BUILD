load("//pycharm_bazel:pycharm_pytest_wrapper.bzl", "pycharm_pytest_wrapper")
load("@pip_shared//:requirements.bzl", "requirement")

py_library(
    name = "customers",
    srcs = [
        "__init__.py",
        "customers_repository.py",
        "in_memory_customers_repository.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//shared/domain/customers",
    ],
)

pycharm_pytest_wrapper(
    name = "test_unit",
    srcs = [
        "test_in_memory_customers_repo.py",
    ],
    args = [
        "-m",
        "unit",
    ],
    data = ["//:pytest_ini"],
    deps = [
        requirement("pytest"),
        ":customers",
        "//shared/domain/customers/definitions:constants",
        "//shared/domain/customers/definitions:fakers",
    ],
)
