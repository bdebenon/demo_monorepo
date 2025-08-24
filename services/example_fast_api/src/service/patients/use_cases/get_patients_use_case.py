from services.example_fast_api.src.domain.patients.definitions.models import Patient
from services.example_fast_api.src.infra.patients.patients_repository import PatientsRepository


class GetPatientsUseCase:
    def __init__(self, patients_repository: PatientsRepository):
        self._patients_repository = patients_repository

    def execute(self, max_age: int) -> list[Patient]:
        return self._patients_repository.get_patients(max_age=max_age)