# Copyright (c) 2024, Rajneesh yadav and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Sum, Coalesce

def execute(filters=None):
    columns = get_columns()
    data = get_data()
    char_data = getChartData(data)
    total_revenue = sum([d.get("revenue", 0) for d in data])

    # Add summary row
    summary_row = {
        "airline": "Total",
        "revenue": total_revenue
    }
    data.append(summary_row)

    return columns, data, None, char_data

def get_columns():
    return [
        {
            "fieldname": "airline",
            "fieldtype": "Link",
            "label": "Airline",
            "options": "Airline",
            "width": 200
        },
        {
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "label": "Revenue",
            "width": 150
        }
    ]

def get_data():
    airplane_ticket = DocType('Airplane Ticket')
    airplane_fights = DocType('Airplane Flight')
    airplane = DocType('Airplane')
    airline = DocType('Airline')
    # Fetch airlines and total revenue from airplane tickets
    query = (
        frappe.qb.from_(airline)
        .left_join(airplane)
        .on(airline.name == airplane.airline)
        .left_join(airplane_fights)
        .on(airplane_fights.airplane == airplane.name)
        .left_join(airplane_ticket)
        .on(airplane_ticket.flight == airplane_fights.name)      
        .select(
            airline.name.as_("airline"),
            Coalesce(Sum(airplane_ticket.total_amount), 0).as_("revenue")
        )
        .groupby(airline.name)
    )

    return query.run(as_dict=True)


def getChartData(data):
  labels = []
  values = []
  
  for data in data:
    labels.append(data.airline)
    values.append(data.revenue)
    
  
  return {
		"data":{
			"labels":labels,
            "datasets":[{
                "values":values
            }]
		},
        "type":"donut"
	}