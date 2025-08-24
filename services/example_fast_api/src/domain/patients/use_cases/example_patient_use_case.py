from services.example_fast_api.src.domain.patients.definitions.models import Patient
from shared.domain.customers.definitions.models import Customer

class ExamplePatientUseCase:
    @staticmethod
    def execute(
            customer: Customer,
            patient: Patient,
    ) -> Customer:
        """
        Example use case just to illustrate using a shared domain model (domain model that can be shared across multiple services).
        """
        assert patient.name != ""
        assert patient.age > 0
        return customer
