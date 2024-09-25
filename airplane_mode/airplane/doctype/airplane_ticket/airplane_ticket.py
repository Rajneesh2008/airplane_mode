# Copyright (c) 2024, Rajneesh Yadav
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        # Call validation for ticket capacity
        self.check_ticket_capacity()
        # Calculate total amount for the ticket
        self.getTotalAmount()

    def check_ticket_capacity(self):
        # Fetching the Flight document linked to this ticket
        flight = frappe.get_doc('Airplane Flight', self.flight)
        
        # Fetching the Airplane document linked to the flight doc * filed flight *
        airplane = frappe.get_doc('Airplane', flight.airplane)

        # Fetched the total number of tickets already created for this flight (single Flight has how many booked tickets)
        total_tickets = frappe.db.count('Airplane Ticket', {'flight': self.flight})

        # validationg if the number of tickets exceeds the capacity of that flight(airplane)
        if total_tickets >= airplane.capacity:
            frappe.throw(f"Cannot create ticket: The airplane has only {airplane.capacity} seats, and all are already booked.")

    def getTotalAmount(self):
        flightPrice = self.flight_price
        totalAddOn = 0

        # Check if the add_ons is empty
        if not self.add_ons:
            self.total_amount = flightPrice
        else:
            singleProduct = set()  # Ensure unique products are processed
            for item in self.add_ons:
                # Check for duplicate add-ons
                if item.item not in singleProduct:
                    singleProduct.add(item.item)
                    totalAddOn += item.amount
                else:
                    # Warn the user about duplicate add-ons
                    frappe.msgprint(f"Duplicate item detected: {item.item} has already been added.")

            # Set the total amount as the sum of flight price and add-ons
            self.total_amount = totalAddOn + flightPrice
