"""
review.py
---------
Implements the Review class.
"""

import uuid
from datetime import date
from guest import Guest

class Review:
    """
    Represents a guest's feedback about their stay.
    """

    def __init__(self, guest: Guest, rating: int, comment: str, review_date: date):
        self._review_id = str(uuid.uuid4())
        self._guest = guest
        self._rating = rating
        self._comment = comment
        self._date = review_date

    def get_review_id(self) -> str:
        return self._review_id

    def get_guest(self) -> Guest:
        return self._guest

    def get_rating(self) -> int:
        return self._rating

    def set_rating(self, rating: int) -> None:
        self._rating = rating

    def get_comment(self) -> str:
        return self._comment

    def set_comment(self, comment: str) -> None:
        self._comment = comment

    def get_date(self) -> date:
        return self._date

    def submit(self) -> None:
        """
        Placeholder for logic to submit a review to a database or system.
        """
        pass

    def __str__(self) -> str:
        return (f"Review [ID={self._review_id}, Guest={self._guest.get_name()}, "
                f"Rating={self._rating}, Date={self._date}]")
