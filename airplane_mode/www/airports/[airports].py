

import frappe


def get_context(context):
    airport = frappe.form_dict.get('airports')

    filters = {}
    if airport:
        filters["source"] = airport

    source = frappe.get_list('Airplane Flight',filters=filters , fields=['airplane','date_of_departure', 'destination', 'status', 'source', 'source_airport_code','destination_airport_code', 'duration'])

    context.source_flights = source
   

    filters = {}
    if airport:
        filters["destination"] = airport
     # Fetch  flights
    destination = frappe.get_list('Airplane Flight',filters=filters , fields=['airplane','date_of_departure', 'destination', 'status', 'source', 'source_airport_code','destination_airport_code', 'duration'])
    
    context.destination_flights = destination
    context.airport = airport
    return context