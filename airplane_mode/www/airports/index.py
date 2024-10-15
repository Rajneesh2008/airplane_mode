import frappe;


def get_context(context):
    city = frappe.form_dict.get("city")

    filters = {}
    if city:
        filters["city"] = city
    print(city)
    airports = frappe.get_list('Airport',
    filters=filters,
    fields =['name','city','code','country'])                        

    context.airports = airports
    
    return context


                               
