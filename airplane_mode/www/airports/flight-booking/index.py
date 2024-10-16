import frappe
import frappe.sessions
import frappe.utils

def get_context(context):

    # Check if the user is logged in
    context.isGuest = False
    if frappe.session.user == "Guest":
        context.isGuest = True
    
    
    # Retrieve CSRF token
    context.csrf = frappe.sessions.get_csrf_token()
    # Retrieve flight name from request parameters
    context.flightName = frappe.form_dict.get("flight")
    return context
