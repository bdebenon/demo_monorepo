load("@pip_example_fast_api//:requirements.bzl", "requirement")

py_library(
    name = "dependency_injection",
    srcs = [
        "__init__.py",
        "container.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        requirement("dependency-injector"),
        "//services/example_fast_api/src/common",
        "//services/example_fast_api/src/infra/patients",
        "//services/example_fast_api/src/domain/patients",
        "//services/example_fast_api/src/domain/patients/definitions:fakers",
        "//shared/infra/customers",
        "//shared/domain/customers/definitions:fakers"
    ],
)
