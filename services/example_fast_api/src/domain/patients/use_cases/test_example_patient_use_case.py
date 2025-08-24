import pytest

from services.example_fast_api.src.domain.patients.definitions.fakers import PatientProvider
from services.example_fast_api.src.domain.patients.use_cases.example_patient_use_case import \
    ExamplePatientUseCase
from shared.domain.customers.definitions.fakers import CustomerProvider


class TestExamplePatientUseCase:
    @pytest.mark.unit
    def test_example_patient_use_case(self):
        customer = CustomerProvider.customer()
        patient = PatientProvider.patient()

        result = ExamplePatientUseCase.execute(
            customer=customer,
            patient=patient,
        )

        assert customer == result


