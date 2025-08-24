import pytest

from services.example_fast_api.src.domain.patients.definitions.fakers import PatientProvider
from services.example_fast_api.src.infra.patients.in_memory_patients_repository import InMemoryPatientsRepository
from services.example_fast_api.src.service.patients.use_cases.get_patients_use_case import GetPatientsUseCase


class TestGetPatientsUseCase:
    @pytest.mark.unit
    def test_get_patients_use_case_execute_no_results(self):
        # Arrange
        patients = [PatientProvider.patient(age=30) for _ in range(10)]
        patients_repository = InMemoryPatientsRepository(data=patients)
        get_patients_use_case = GetPatientsUseCase(patients_repository=patients_repository)

        # Act
        received_patients = get_patients_use_case.execute(max_age=29)

        # Assert
        assert len(received_patients) == 0

    @pytest.mark.unit
    def test_get_patients_use_case_execute_all_results(self):
        # Arrange
        patients = [PatientProvider.patient(age=30) for _ in range(10)]
        patients_repository = InMemoryPatientsRepository(data=patients)
        get_patients_use_case = GetPatientsUseCase(patients_repository=patients_repository)

        # Act
        received_patients = get_patients_use_case.execute(max_age=30)

        # Assert
        assert len(received_patients) == len(patients)