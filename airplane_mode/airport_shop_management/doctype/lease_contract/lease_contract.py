# Copyright (c) 2024, Rajneesh yadav and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class LeaseContract(Document):
    
    def before_save(self):
        # Debugging output to ensure the method is called
        print(f"Checking if a lease contract exists for Shop: {self.shop}")
        
        # Check if a lease contract already exists for the selected shop
        existing_lease = frappe.db.exists('Lease Contract', {
            'shop': self.shop
        })

        # Debugging output to see the result of the query
        print(f"Existing Lease: {existing_lease}")
        
        if existing_lease:
            frappe.throw(f"A lease contract already exists for Shop {self.shop}.")
