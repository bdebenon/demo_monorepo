requirements:
	(cat requirements.txt; echo ""; cat requirements_test.txt) > requirements_combined.in
	# Ensure that the requirements_lock file exists or requirements.update will fail
	echo "" > requirements_lock.txt
	bazel run //shared:requirements.update

test-unit:
	bazel test //shared:test_unit
