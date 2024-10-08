import frappe



def get_context(context):
    
    shop_name = frappe.form_dict.get("shop_id")

    if shop_name:
        try:
            shop = frappe.get_doc("Shop",shop_name)
            context.shop = shop

        except frappe.DoesNotExistError:
            frappe.throw(f"shop with id {shop_name} is not present in database")
    
    
    return context