from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from shared.domain.customers.definitions.models import Customer


class CustomersRepository(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_customer(self, uuid: UUID) -> Optional[Customer]:
        pass

    @abstractmethod
    def get_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def delete_customer(self, customer: Customer):
        pass
