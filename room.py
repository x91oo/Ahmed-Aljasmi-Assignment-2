"""
room.py
-------
Implements the Room class.
"""

from __future__ import annotations
from datetime import date

class Room:
    """
    The Room class holds details about a hotel room,
    including its ID, type, amenities, price, and bookings.
    """

    def __init__(self, room_id: str, room_type: str, amenities: list, price_per_night: float):
        self._room_id = room_id
        self._room_type = room_type
        self._amenities = amenities
        self._price_per_night = price_per_night
        # We'll store a list of Reservation objects (forward reference to avoid circular import)
        self._bookings = []

    def get_room_id(self) -> str:
        return self._room_id

    def set_room_id(self, room_id: str) -> None:
        self._room_id = room_id

    def get_room_type(self) -> str:
        return self._room_type

    def set_room_type(self, room_type: str) -> None:
        self._room_type = room_type

    def get_amenities(self) -> list:
        return self._amenities

    def set_amenities(self, amenities: list) -> None:
        self._amenities = amenities

    def get_price_per_night(self) -> float:
        return self._price_per_night

    def set_price_per_night(self, price: float) -> None:
        self._price_per_night = price

    def get_bookings(self) -> list:
        return self._bookings

    def add_booking(self, reservation) -> None:
        """
        Add a Reservation object to the room's bookings list.
        """
        self._bookings.append(reservation)

    def is_available(self, start: date, end: date) -> bool:
        """
        Checks if the room is available for the given date range.
        Returns True if available, False otherwise.
        """
        for booking in self._bookings:
            if not booking.is_cancelled():
                # If there's an overlap, the room isn't available
                if start < booking.get_check_out() and end > booking.get_check_in():
                    return False
        return True

    def __str__(self) -> str:
        return (f"Room [ID={self._room_id}, Type={self._room_type}, "
                f"Price={self._price_per_night}, Amenities={self._amenities}]")
