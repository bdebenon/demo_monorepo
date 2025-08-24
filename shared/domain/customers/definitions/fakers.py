from uuid import uuid4, UUID

from faker import Faker

from shared.domain.customers.definitions.models import Customer

fake = Faker()


class CustomerProvider:
    @staticmethod
    def customer(
            uuid: UUID = None,
            name: str = None,
    ) -> Customer:
        fake_name = fake.name()
        return Customer(
            uuid=uuid if uuid else uuid4(),
            name=name if name else fake_name,
            display_name=name if name else fake_name,
            client_id=name if name else fake_name,
        )
