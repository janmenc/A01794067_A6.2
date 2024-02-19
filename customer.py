"""Class that creates and deletes a Customer object
with some methods to make unit tests
"""
import unittest


class Customer:
    """Customer class"""
    def __init__(self, customer_id, name, email):
        """Function that create an object"""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Function that create a dictionary"""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
        }


class CustomerManager:
    """Customer Manager class that manages the customer object"""
    def __init__(self):
        self.customers = []

    def create_customer(self, customer_id, name, email):
        """Function that creates a customer"""
        customer = Customer(customer_id, name, email)
        self.customers.append(customer)
        return customer

    def delete_customer(self, customer):
        """Function that deletes a customer"""
        if customer in self.customers:
            self.customers.remove(customer)
        else:
            raise ValueError("Customer not found")

    def display_customer_info(self, customer):
        """Function that displays a customer"""
        return customer.to_dict()

    def modify_customer_info(self, customer, new_name, new_email):
        """Function that modifies a customer"""
        customer.name = new_name
        customer.email = new_email


class TestCustomerMethods(unittest.TestCase):
    """Test unit class class"""
    def setUp(self):
        """Function that sets an object"""
        self.customer_manager = CustomerManager()
        self.customer = self.customer_manager.create_customer(1, "John Doe", "john@example.com")

    def test_create_customer(self):
        """Function that test create object"""
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john@example.com")

    def test_modify_customer_info(self):
        """Function that test modify object"""
        self.customer_manager.modify_customer_info(self.customer, "Updated Name", "updated@example.com")
        self.assertEqual(self.customer.name, "Updated Name")
        self.assertEqual(self.customer.email, "updated@example.com")

    def test_delete_customer(self):
        """Function that test delete object"""
        self.customer_manager.delete_customer(self.customer)
        with self.assertRaises(ValueError) as context:
            self.customer_manager.delete_customer(self.customer)
        self.assertEqual(str(context.exception), "Customer not found")

    def test_display_customer_info(self):
        """Function that test display object"""
        info = self.customer_manager.display_customer_info(self.customer)
        expected_info = {"customer_id": 1, "name": "John Doe", "email": "john@example.com"}
        self.assertEqual(info, expected_info)


if __name__ == '__main__':
    unittest.main()
