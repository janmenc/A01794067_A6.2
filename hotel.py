"""Class that creates and deletes a Hotel object
with some methods to make unit tests
"""
import unittest


class Hotel:
    """Hotel class with methods create a object, create
    reservation and cancel reservation
    """
    def __init__(self, hotel_id, name, rooms):
        """Function that create an object"""
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def to_dict(self):
        """Function that create a dictionary"""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "rooms": self.rooms,
            "reservations": [res.to_dict() for res in self.reservations],
        }

    def reserve_room(self, reservation_id, customer):
        """Function that makes a reservation"""
        # Assuming reservation_id is unique
        reservation = Reservation(reservation_id, customer, self)
        self.reservations.append(reservation)
        return reservation

    def cancel_reservation(self, reservation):
        """Function that cancels a reservation"""
        if reservation in self.reservations:
            self.reservations.remove(reservation)
        else:
            raise ValueError("Reservation not found")


class Reservation:
    """Reservation class"""
    def __init__(self, reservation_id, customer, hotel):
        """Function that create a reservation"""
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


class TestHotelMethods(unittest.TestCase):
    """Test unit class class"""
    def setUp(self):
        """Function that sets an object"""
        self.hotel = Hotel(1, "Sample Hotel", 10)

    def test_create_hotel(self):
        """Function that test create object"""
        self.assertEqual(self.hotel.name, "Sample Hotel")
        self.assertEqual(self.hotel.rooms, 10)

    def test_modify_hotel_info(self):
        """Function that test modify info"""
        self.hotel.name = "Updated Hotel"
        self.hotel.rooms = 20
        self.assertEqual(self.hotel.name, "Updated Hotel")
        self.assertEqual(self.hotel.rooms, 20)

    def test_reserve_and_cancel_reservation(self):
        """Function that test cancel reservation"""
        customer = Customer(1, "John Doe", "john@example.com")
        reservation_id = "123"
        reservation = self.hotel.reserve_room(reservation_id, customer)

        self.assertEqual(len(self.hotel.reservations), 1)

        self.hotel.cancel_reservation(reservation)
        self.assertEqual(len(self.hotel.reservations), 0)

    def test_cancel_nonexistent_reservation(self):
        """Function that test a negative case"""
        customer = Customer(1, "John Doe", "john@example.com")
        reservation_id = "123"
        reservation = Reservation(reservation_id, customer, self.hotel)

        # Adding reservation to the hotel is intentionally skipped

        with self.assertRaises(ValueError) as context:
            self.hotel.cancel_reservation(reservation)

        self.assertEqual(str(context.exception), "Reservation not found")


class Customer:
    """Customer class"""
    def __init__(self, customer_id, name, email):
        """Function that create a customer"""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Function that creates a dictionary"""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
        }


if __name__ == '__main__':
    unittest.main()
