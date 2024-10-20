

import frappe
import frappe.sessions

def get_context(context):
    csrf = frappe.sessions.get_csrf_token()

    if(csrf):
        context.csrf_token = csrf

    
    return context