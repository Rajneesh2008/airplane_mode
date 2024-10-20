# Copyright (c) 2024, Rajneesh yadav and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
from frappe.utils import getdate,relativedelta

class LeaseContract(Document):
    def validate(self):
        # parse the dates
        contractStartDate = getdate(self.contract_start_date)
        contractExpireDate = getdate(self.contract_expiry_date)
        print(contractExpireDate,contractStartDate, "Hello from line 11")
        # Ensure contract start date is not greater than contract expire date
        if contractStartDate >= contractExpireDate:
            print("hello from line 15")
            frappe.throw("Contract expire date should be greater than contract start date")
        
        # Ensure there is at least a 6-month difference between start and expire dates
        if (contractExpireDate - contractStartDate).days < 180:  # Roughly 6 months
            print("hello from line 19")
            frappe.throw("Minimum contract duration should be 6 months")

        # Calculate the duration in years and months

        delta = relativedelta(contractExpireDate, contractStartDate)
        self.contract_duration = f"{delta.years} years, {delta.months} months, {delta.days} days "
       

    def before_save(self):
        # Debugging output to ensure the method is called
        print(f"Checking if a lease contract exists for Shop: {self.shop}")
        
        # Check if a lease contract already exists for the selected shop
        existing_lease = frappe.db.exists('Lease Contract', {
            'shop': self.shop,
            'name': ['!=', self.name]
        })

        print(f"Existing Lease: {existing_lease}")
        
        if existing_lease:
            frappe.throw(f"A lease contract already exists for Shop {self.shop}.")
