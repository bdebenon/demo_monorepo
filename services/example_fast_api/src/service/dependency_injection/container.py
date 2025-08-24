from uuid import UUID

from dependency_injector import containers, providers

from services.example_fast_api.src.common.config import config
from services.example_fast_api.src.domain.patients.definitions.fakers import PatientProvider
from services.example_fast_api.src.domain.patients.use_cases.example_patient_use_case import ExamplePatientUseCase
from services.example_fast_api.src.infra.patients.in_memory_patients_repository import InMemoryPatientsRepository
from services.example_fast_api.src.service.patients.use_cases.get_patients_use_case import GetPatientsUseCase
from shared.domain.customers.definitions.fakers import CustomerProvider
from shared.domain.customers.definitions.models import Customer
from shared.infra.customers.in_memory_customers_repository import InMemoryCustomersRepository


class Container(containers.DeclarativeContainer):
    # Config Values
    test_config_key = config.get_config_by_section_and_key(
        section_name='test', key='test_key')

    # Domain Use Cases
    example_patient_use_case = providers.Singleton(
        ExamplePatientUseCase
    )

    # Infra Repositories
    customer: Customer = CustomerProvider.customer(
        uuid=UUID('15517a1a-51cb-44a5-a22d-94c8712500c3'),
        name="Example Customer Name",
    )
    customers_repository = providers.Singleton(
        InMemoryCustomersRepository,
        data={customer.uuid: customer},
    )
    patients_repository = providers.Singleton(
        InMemoryPatientsRepository,
        data=[PatientProvider.patient(age=30) for _ in range(10)],
    )

    # Service Layer Repos
    get_patients_use_case = providers.Singleton(
        GetPatientsUseCase,
        patients_repository=patients_repository,
    )
