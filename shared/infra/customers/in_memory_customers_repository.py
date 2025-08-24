from typing import List, Dict, Optional
from uuid import UUID

from shared.domain.customers.definitions.models import Customer
from shared.infra.customers.customers_repository import CustomersRepository


class InMemoryCustomersRepository(CustomersRepository):
    def __init__(self, data: Dict = None):
        self._data: Dict[UUID, Customer] = data if data else {}

    def add_customer(self, customer: Customer) -> None:
        self._data[customer.uuid] = customer

    def get_customer(self, uuid: UUID) -> Optional[Customer]:
        return self._data.get(uuid)

    def get_customers(self) -> List[Customer]:
        return [self._data[customer] for customer in self._data]

    def delete_customer(self, customer: Customer):
        del self._data[customer.uuid]
