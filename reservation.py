"""Class that creates and deletes a Reservation object
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


class Hotel:
    """Hotel class with methods create a object, create
    reservation and cancel reservation
    """
    def __init__(self, hotel_id, name, rooms):
        """Function that create an object"""
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms

    def to_dict(self):
        """Function that create a dictionary"""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "rooms": self.rooms,
        }


class Reservation:
    """Reservation class with methods create an object
    and create a dictionary
    """
    def __init__(self, reservation_id, customer, hotel):
        """Function that create an object"""
        self.reservation_id = reservation_id
        self.customer = customer
        self.hotel = hotel

    def to_dict(self):
        """Function that create a dictionary"""
        return {
            "reservation_id": self.reservation_id,
            "customer": self.customer.to_dict(),
            "hotel": self.hotel.to_dict(),
        }


class ReservationManager:
    """Customer Manager class that manages the customer object"""
    def __init__(self):
        """Function that create an object"""
        self.reservations = []

    def create_reservation(self, reservation_id, customer, hotel):
        """Function that creates a reservation"""
        reservation = Reservation(reservation_id, customer, hotel)
        self.reservations.append(reservation)
        return reservation

    def cancel_reservation(self, reservation):
        """Function that cancels a reservation"""
        if reservation in self.reservations:
            self.reservations.remove(reservation)
        else:
            raise ValueError("Reservation not found")


class TestReservationMethods(unittest.TestCase):
    """Test unit class class"""
    def setUp(self):
        """Function that sets an object"""
        self.customer = Customer(1, "John Doe", "john@example.com")
        self.hotel = Hotel(1, "Sample Hotel", 10)
        self.reservation_manager = ReservationManager()

    def test_create_reservation(self):
        """Function that test create object"""
        reservation = self.reservation_manager.create_reservation(1, self.customer, self.hotel)
        self.assertEqual(reservation.reservation_id, 1)
        self.assertEqual(reservation.customer, self.customer)
        self.assertEqual(reservation.hotel, self.hotel)

    def test_cancel_reservation(self):
        """Function that test cancel object"""
        reservation = self.reservation_manager.create_reservation(1, self.customer, self.hotel)
        self.reservation_manager.cancel_reservation(reservation)
        self.assertEqual(len(self.reservation_manager.reservations), 0)

    def test_cancel_nonexistent_reservation(self):
        """Function that test a negative case"""
        reservation = Reservation(1, self.customer, self.hotel)

        # Adding reservation to the manager is intentionally skipped

        with self.assertRaises(ValueError) as context:
            self.reservation_manager.cancel_reservation(reservation)

        self.assertEqual(str(context.exception), "Reservation not found")


if __name__ == '__main__':
    unittest.main()
