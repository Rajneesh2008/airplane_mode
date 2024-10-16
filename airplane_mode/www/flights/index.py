import frappe
from frappe.utils import today

def get_context(context):

    filters = {}

    source = frappe.form_dict.get("source_city")
    destination = frappe.form_dict.get("destination_city")
    date_of_departure = frappe.form_dict.get("departure")

    if source:
        filters["source_city"] = source
        context.source = source
    
    if destination:
        filters["destination_city"] = destination
        context.destination = destination
    
    if date_of_departure:
        filters["date_of_departure"] = ['>=', date_of_departure]
        context.date_of_departure = date_of_departure
    else:
        filters["date_of_departure"] = ['>=', today()]
    print(filters)

    flights = frappe.db.get_list("Airplane Flight",filters=filters,fields=['airplane','name','date_of_departure', 'destination', 'status', 'source', 'source_airport_code','destination_airport_code', 'duration'],order_by=date_of_departure)

    print(flights)
    if flights:
        context.flights = flights
    else:
        context.isAvailable = False
    
    return context
