"""
reservation.py
--------------
Implements the Reservation class.
"""

from __future__ import annotations
from datetime import date
from guest import Guest
from room import Room

class Reservation:
    """
    The Reservation class ties a guest to a room
    for a specified date range, with a status indicating
    whether it's active or cancelled.
    """

    def __init__(self, res_id: str, guest: Guest, room: Room, check_in: date, check_out: date):
        self._res_id = res_id
        self._guest = guest
        self._room = room
        self._check_in = check_in
        self._check_out = check_out
        self._status = "CONFIRMED"

        # Add this reservation to the room's booking list
        room.add_booking(self)

    def get_res_id(self) -> str:
        return self._res_id

    def get_guest(self) -> Guest:
        return self._guest

    def get_room(self) -> Room:
        return self._room

    def get_check_in(self) -> date:
        return self._check_in

    def get_check_out(self) -> date:
        return self._check_out

    def is_cancelled(self) -> bool:
        return self._status == "CANCELLED"

    def calculate_total(self) -> float:
        """
        Calculate total cost based on (number of nights * room price).
        """
        nights = (self._check_out - self._check_in).days
        return self._room.get_price_per_night() * nights

    def cancel(self) -> None:
        """
        Cancels the reservation by updating its status.
        """
        self._status = "CANCELLED"

    def __str__(self) -> str:
        return (f"Reservation [ID={self._res_id}, Guest={self._guest.get_name()}, "
                f"Room={self._room.get_room_id()}, Status={self._status}]")
