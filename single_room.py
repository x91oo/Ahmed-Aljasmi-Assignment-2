"""
single_room.py
--------------
Implements the SingleRoom class, which inherits from Room.
"""

from room import Room

class SingleRoom(Room):
    """
    SingleRoom is a specialized Room that may include
    unique methods or properties.
    """

    def __init__(self, room_id: str, amenities: list, price_per_night: float):
        # Hard-code "Single" as room_type for single rooms
        super().__init__(room_id, "Single", amenities, price_per_night)

    def get_special_offer(self) -> str:
        """
        Returns a string describing a special offer for single rooms.
        """
        return "Special Offer: Stay 3 nights in a Single Room and get 10% off your total bill!"
