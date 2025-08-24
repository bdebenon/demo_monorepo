PROJECT=example_fast_api
VERSION=local

requirements:
	(cat requirements.txt; echo ""; cat requirements_test.txt) > requirements_combined.in
	# Ensure that the requirements_lock file exists or requirements.update will fail
	echo "" > requirements_lock.txt
	bazel run //services/example_fast_api:requirements.update

run-terminal:
	bazel run //services/example_fast_api/src/service:app

test-unit:
	bazel test --test_output=all //services/example_fast_api:test_unit

test-unit-docker:
	docker run --entrypoint bazel ${PROJECT}:${VERSION} test --test_output=all //services/example_fast_api:test_unit

test-all:
	bazel test --test_output=all //services/example_fast_api:test_all

# Docker
build:
	cd .. && cd .. && ls && \
	docker build -t ${PROJECT}:${VERSION} -f services/example_fast_api/Dockerfile .

local-delete-running-containers:
	docker kill ${PROJECT} || true  # continue even if command fails
	docker rm ${PROJECT} || true

run-docker:
	make local-delete-running-containers
	docker run -p 8002:3000 --name ${PROJECT} ${PROJECT}:${VERSION}
