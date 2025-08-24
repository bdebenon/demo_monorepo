import pytest

from services.example_fast_api.src.domain.patients.definitions.fakers import PatientProvider
from services.example_fast_api.src.infra.patients.in_memory_patients_repository import \
    InMemoryPatientsRepository


class TestInMemoryPatientsRepository:


    data = [
        PatientProvider.patient(age=10),
        PatientProvider.patient(age=100),
    ]

    @pytest.mark.unit
    def test_get_patients_one_result(self):
        max_age = 10
        patients_repository = InMemoryPatientsRepository(data=self.data)

        retrieved_patients = patients_repository.get_patients(max_age=max_age)

        assert len(retrieved_patients) == 1
        for patient in retrieved_patients:
            assert patient.age <= max_age

    @pytest.mark.unit
    def test_get_patients_two_result(self):
        max_age = 100
        patients_repository = InMemoryPatientsRepository(data=self.data)

        retrieved_patients = patients_repository.get_patients(max_age=max_age)

        assert len(retrieved_patients) == 2
        for patient in retrieved_patients:
            assert patient.age <= max_age
