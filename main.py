# main.py
from datetime import date
from guest import Guest
from single_room import SingleRoom
from reservation import Reservation
from invoice import Invoice
from payment import Payment

def test_case_ahmed():
    print("----- Test Case: Ahmed Al Jasmi -----")
    
    # Create guest account for Ahmed Al Jasmi
    ahmed = Guest("G001", "Ahmed Al Jasmi", "ahmed@example.com", "555-1234", "securepass")
    print("Guest Created:", ahmed)
    
    # Create a SingleRoom instance
    room_101 = SingleRoom("R101", ["Wi-Fi", "TV", "Mini-Bar"], 120.0)
    print("Room Details:", room_101)
    
    # Define Ahmed's desired booking dates: April 10, 2025 to April 15, 2025
    check_in = date(2025, 4, 10)
    check_out = date(2025, 4, 15)
    
    # Check room availability and create reservation if available
    if room_101.is_available(check_in, check_out):
        reservation_ahmed = Reservation("RES001", ahmed, room_101, check_in, check_out)
        print("Reservation Created:", reservation_ahmed)
        
        # Generate invoice for the reservation
        invoice_ahmed = Invoice(reservation_ahmed)
        invoice_str = invoice_ahmed.generate()
        print("Invoice Details:\n", invoice_str)
        
        # Process payment for the invoice using Credit Card method
        payment_ahmed = Payment(invoice_ahmed.get_total_amount(), "Credit Card")
        if payment_ahmed.process():
            print("Payment processed successfully for Ahmed Al Jasmi.\n")
        else:
            print("Payment processing failed for Ahmed Al Jasmi.\n")
    else:
        print("Room is not available for Ahmed's selected dates.\n")

def test_case_sultan():
    print("----- Test Case: Sultan Allanjawi -----")
    
    # Create guest account for Sultan Allanjawi
    sultan = Guest("G002", "Sultan Allanjawi", "sultan@example.com", "555-5678", "mypassword")
    print("Guest Created:", sultan)
    
    # Create a different SingleRoom instance for variety
    room_102 = SingleRoom("R102", ["Wi-Fi", "TV"], 100.0)
    print("Room Details:", room_102)
    
    # Define Sultan's desired booking dates: April 12, 2025 to April 18, 2025
    check_in = date(2025, 4, 12)
    check_out = date(2025, 4, 18)
    
    # Check room availability and create reservation if available
    if room_102.is_available(check_in, check_out):
        reservation_sultan = Reservation("RES002", sultan, room_102, check_in, check_out)
        print("Reservation Created:", reservation_sultan)
        
        # Generate invoice for the reservation
        invoice_sultan = Invoice(reservation_sultan)
        invoice_str = invoice_sultan.generate()
        print("Invoice Details:\n", invoice_str)
        
        # Process payment for the invoice using Mobile Wallet method
        payment_sultan = Payment(invoice_sultan.get_total_amount(), "Mobile Wallet")
        if payment_sultan.process():
            print("Payment processed successfully for Sultan Allanjawi.\n")
        else:
            print("Payment processing failed for Sultan Allanjawi.\n")
    else:
        print("Room is not available for Sultan's selected dates.\n")

def main():
    test_case_ahmed()
    test_case_sultan()

if __name__ == "__main__":
    main()
