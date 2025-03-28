"""
guest_service_request.py
------------------------
Implements the GuestServiceRequest class.
"""

import uuid
from datetime import datetime
from guest import Guest

class GuestServiceRequest:
    """
    Represents a request by a guest for an additional service,
    such as housekeeping, room service, or transportation.
    """

    def __init__(self, guest: Guest, request_type: str, details: str):
        self._request_id = str(uuid.uuid4())
        self._guest = guest
        self._type = request_type
        self._details = details
        self._timestamp = datetime.now()
        self._status = "OPEN"

    def get_request_id(self) -> str:
        return self._request_id

    def get_guest(self) -> Guest:
        return self._guest

    def get_type(self) -> str:
        return self._type

    def get_details(self) -> str:
        return self._details

    def get_timestamp(self) -> datetime:
        return self._timestamp

    def get_status(self) -> str:
        return self._status

    def submit(self) -> None:
        """
        Placeholder for logic to submit the request to hotel staff.
        """
        self._status = "SUBMITTED"

    def __str__(self) -> str:
        return (f"GuestServiceRequest [ID={self._request_id}, Guest={self._guest.get_name()}, "
                f"Type={self._type}, Status={self._status}]")
