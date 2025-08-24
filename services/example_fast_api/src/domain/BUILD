py_library(
    name = "domain",
    srcs = [
        "__init__.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//services/example_fast_api/src/domain/patients",
    ],
)

test_suite(
    name = "test_unit",
    tests = [
        "//services/example_fast_api/src/domain/patients/definitions:test_unit",
        "//services/example_fast_api/src/domain/patients/use_cases:test_unit",
    ],
)
