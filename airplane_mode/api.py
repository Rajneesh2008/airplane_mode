# In your_app/api.py
import frappe

@frappe.whitelist(allow_guest=True)
def create_ticket(flight_name, passenger_name):
    
    print(flight_name,passenger_name)
    # Fetch related flight details
    flight_doc = frappe.get_doc("Airplane Flight", flight_name)
 
    # Create a new ticket with the fetched details
    new_ticket = frappe.get_doc({
        "doctype": "Airplane Ticket",
        "flight": flight_name,
        "passenger": passenger_name,
        "departure_date": flight_doc.date_of_departure,
        "departure_time": flight_doc.time_of_departure,
        "destination_airport_code":flight_doc.destination_airport_code,
        "docstatus":0,
        "duration_of_flight":flight_doc.duration,
        "flight_price":flight_doc.amount,
        "gate_no":flight_doc.gate_no,
        "source_airport_code":flight_doc.source_airport_code,
        "status":"Booked"
        # Add other necessary fields here
    })
    new_ticket.insert()
    frappe.db.commit()
    return {"status": "success", "message": "Ticket booked"}
