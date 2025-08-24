# Shared code

## Updating dependencies (requirements)

In order to update the dependencies utilized by this package, you will need to have Bazel update
the `requirements_lock.txt` file.

This can be achieved by the following steps:

1. Add/Remove/Update a dependency in the `requirements.txt` or the `test-requirements.txt` files
2. Run `make requirements` from within the `shared` folder.

This will update the `requirements_lock.txt` file with any dependency changes.

## Running tests

### Unit tests

```
make test_unit
```