import frappe;


def get_context(context):
    
    airports = frappe.get_list('Airport',
    fields =['name','city','code','country'])                        

    context.airports = airports
    
    return context


                               
