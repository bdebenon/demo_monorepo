from uuid import UUID

import pytest

from shared.domain.customers.definitions.constants import TEST_CUSTOMER_NAME
from shared.domain.customers.definitions.fakers import CustomerProvider
from shared.domain.customers.definitions.models import Customer
from shared.infra.customers.in_memory_customers_repository import InMemoryCustomersRepository

uuid = UUID('15517a1a-51cb-44a5-a22d-94c8712500c3')


class TestInMemoryCustomersRepo:
    @pytest.mark.unit
    def test_add_customer(self):
        customers_repository = InMemoryCustomersRepository()

        new_customer: Customer = CustomerProvider.customer(uuid=uuid, name=TEST_CUSTOMER_NAME)

        customers_repository.add_customer(customer=new_customer)

        assert new_customer.uuid in customers_repository._data
        assert customers_repository._data[new_customer.uuid].uuid == new_customer.uuid
        assert customers_repository._data[new_customer.uuid].name == new_customer.name
        assert customers_repository._data[new_customer.uuid].display_name == new_customer.display_name

    @pytest.mark.unit
    def test_get_customer(self):
        expected_customer = CustomerProvider.customer(uuid=uuid, name=TEST_CUSTOMER_NAME)

        data = {
            expected_customer.uuid: expected_customer
        }
        customers_repository = InMemoryCustomersRepository(data=data)

        actual_customer = customers_repository.get_customer(uuid=expected_customer.uuid)

        assert expected_customer == actual_customer

    @pytest.mark.unit
    def test_get_customers(self):
        new_customer_1 = CustomerProvider.customer(uuid=uuid, name=TEST_CUSTOMER_NAME)
        new_customer_2 = CustomerProvider.customer(uuid=uuid, name=TEST_CUSTOMER_NAME)

        data = {
            new_customer_1.uuid: new_customer_1,
            new_customer_2.uuid: new_customer_2
        }
        customers_repository = InMemoryCustomersRepository(data=data)

        customers = customers_repository.get_customers()

        for customer in customers:
            assert isinstance(customer, Customer)

    @pytest.mark.integration
    def test_delete_customer(self):
        customers_repository = InMemoryCustomersRepository()

        new_customer = CustomerProvider.customer(uuid=uuid, name=TEST_CUSTOMER_NAME)

        # We have to add the customer first to test the delete function.
        # The purpose of this test is not to test the 'add_customer' function though
        customers_repository.add_customer(customer=new_customer)

        customers_repository.delete_customer(customer=new_customer)
