# Example Fast API

Example FastAPI API service 

## Notable API Endpoints

### Documentation

URL Format: `[BASE_URL]/docs`

Example: `http://127.0.0.1:8002/docs`

## Prerequisites

Because we are using Bazel, we will need to build the pip packages into wheels.

The following commands will install the dependencies needed to build the pip wheels locally for the dependent
pip
packages.

```bash
sudo apt-get update
sudo apt-get install python3.11-dev
sudo apt-get -y install clang
```

## Setup/Run Instructions

### Setting up Bazel

For instructions on setting up Bazel, see the [README.md](../README.md) in the root of the repository.

### Updating dependencies (requirements)

In order to update the dependencies utilized by this package, you will need have Bazel update
the `requirements_lock.txt` file.

This can be achieved by the following steps:

1. Add/Remove/Update a dependency in the `requirements.txt` or the `test-requirements.txt` files
2. Run `make requirements` from within the `example_fast_api` folder.

This will update the `requirements_lock.txt` file with any dependency changes.

### Running Application

```
make run-terminal
```

### Running tests

#### Unit tests

```
make test-unit
```

#### Integration tests

```
make test-intgration
```

### Docker

#### Running docker interactive bash shell

```bash
docker run -it --name ${PROJECT} ${PROJECT}:${VERSION} bash
```

## References

- FastAPI: https://fastapi.tiangolo.com/
- Python Dependency Injector: https://python-dependency-injector.ets-labs.org/index.html

