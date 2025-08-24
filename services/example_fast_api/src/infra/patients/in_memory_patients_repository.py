from services.example_fast_api.src.domain.patients.definitions.models import Patient
from services.example_fast_api.src.infra.patients.patients_repository import PatientsRepository


class InMemoryPatientsRepository(PatientsRepository):

    def __init__(self, data: list[Patient] = None):
        self._data = data if data else []

    def get_patients(self, max_age: int) -> list[Patient]:
        results = []
        for entry in self._data:
            if entry.age <= max_age:
                results.append(entry)
        return results
