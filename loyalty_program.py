"""
loyalty_program.py
------------------
Implements the LoyaltyProgram class.
"""

class LoyaltyProgram:
    """
    The LoyaltyProgram class handles reward points
    and redemption for a guest.
    """

    def __init__(self):
        self._points = 0

    def get_points(self) -> int:
        return self._points

    def add_points(self, nights: int) -> None:
        """
        Adds points based on the number of nights stayed.
        For example, 10 points per night.
        """
        self._points += nights * 10

    def redeem(self, points: int) -> float:
        """
        Redeems a certain number of points for a discount.
        For example, each point might equal $0.5 discount.
        """
        if points > self._points:
            points = self._points
        discount = points * 0.5
        self._points -= points
        return discount

    def get_available_rewards(self) -> list:
        """
        Placeholder for returning a list of available reward offers.
        """
        return ["10% off next booking", "Free room upgrade"]

    def __str__(self) -> str:
        return f"LoyaltyProgram [Points={self._points}]"
