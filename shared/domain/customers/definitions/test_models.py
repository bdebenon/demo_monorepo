import pytest

from shared.domain.customers.definitions.fakers import CustomerProvider


class TestModels:
    @pytest.mark.unit
    def test_customer_model(self):
        customer = CustomerProvider.customer()
        assert isinstance(customer.name, str)

    @pytest.mark.unit
    def test_customer_model_with_specific_name(self):
        specific_name = 'BBQ Guys'
        customer_with_specific_name = CustomerProvider.customer(name=specific_name)
        assert customer_with_specific_name.name == specific_name
        assert customer_with_specific_name.display_name == specific_name
