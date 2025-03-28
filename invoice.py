"""
invoice.py
----------
Implements the Invoice class.
"""

import uuid
from reservation import Reservation

class Invoice:
    """
    The Invoice class represents billing details
    for a specific reservation.
    """

    def __init__(self, reservation: Reservation, tax: float = 0.05, discount_applied: float = 0.0):
        self._invoice_id = str(uuid.uuid4())
        self._reservation = reservation
        self._tax = tax
        self._discount_applied = discount_applied
        self._total_amount = 0.0

    def get_invoice_id(self) -> str:
        return self._invoice_id

    def get_reservation(self) -> Reservation:
        return self._reservation

    def get_total_amount(self) -> float:
        return self._total_amount

    def generate(self) -> str:
        """
        Generates a summary of the invoice, including total cost, tax, discount, etc.
        """
        base_total = self._reservation.calculate_total()
        taxed_amount = base_total * (1 + self._tax)
        final_amount = taxed_amount - self._discount_applied
        self._total_amount = final_amount

        invoice_str = (
            f"--- Invoice ---\n"
            f"Invoice ID: {self._invoice_id}\n"
            f"Reservation ID: {self._reservation.get_res_id()}\n"
            f"Base Cost: {base_total:.2f}\n"
            f"Tax: {self._tax * 100:.1f}%\n"
            f"Discount: {self._discount_applied:.2f}\n"
            f"Total Due: {final_amount:.2f}\n"
        )
        return invoice_str

    def __str__(self) -> str:
        return f"Invoice [ID={self._invoice_id}, Reservation={self._reservation.get_res_id()}]"
