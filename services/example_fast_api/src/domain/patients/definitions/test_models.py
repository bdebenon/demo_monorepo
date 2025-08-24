import pytest

from services.example_fast_api.src.domain.patients.definitions.fakers import PatientProvider


class TestPatient:
    @pytest.mark.unit
    def test_calculate_something(self):
        patient = PatientProvider.patient()

        result = patient.calculate_something()

        assert isinstance(result, int)
