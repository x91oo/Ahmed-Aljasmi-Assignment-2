"""
guest.py
--------
Implements the Guest class.
"""

from loyalty_program import LoyaltyProgram

class Guest:
    """
    The Guest class holds personal information and references
    a loyalty program for reward points.
    """

    def __init__(self, guest_id: str, name: str, email: str, phone: str, password: str):
        self._guest_id = guest_id
        self._name = name
        self._email = email
        self._phone = phone
        self._password = password
        self._loyalty_program = LoyaltyProgram()  # Each guest can have a loyalty program

    def get_guest_id(self) -> str:
        return self._guest_id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str) -> None:
        self._email = email

    def get_phone(self) -> str:
        return self._phone

    def set_phone(self, phone: str) -> None:
        self._phone = phone

    def get_loyalty_program(self) -> LoyaltyProgram:
        return self._loyalty_program

    def register(self) -> bool:
        """
        Placeholder for registration logic (e.g., saving to a database).
        Returns True if registration is successful.
        """
        return True

    def login(self, email: str, pw: str) -> bool:
        """
        Placeholder for login logic. Returns True if credentials match.
        """
        return (self._email == email and self._password == pw)

    def view_reservation_history(self) -> list:
        """
        Placeholder for returning the guest's past reservations.
        Could be retrieved from a database or manager class.
        """
        return []

    def __str__(self) -> str:
        return f"Guest [ID={self._guest_id}, Name={self._name}, Email={self._email}]"
