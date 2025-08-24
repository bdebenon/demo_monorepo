from abc import abstractmethod, ABC

from services.example_fast_api.src.domain.patients.definitions.models import Patient


class PatientsRepository(ABC):
    @abstractmethod
    def get_patients(self, max_age: int) -> list[Patient]:
        pass
