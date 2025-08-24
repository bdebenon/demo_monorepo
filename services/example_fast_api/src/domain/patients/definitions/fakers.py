from services.example_fast_api.src.domain.patients.definitions.models import Patient


class PatientProvider:
    @staticmethod
    def patient(
            name: str = None,
            age: int = None,
    ) -> Patient:
        return Patient(
            name="John Cena" if name is None else name,
            age=30 if age is None else age,
        )
