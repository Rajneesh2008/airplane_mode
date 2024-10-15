import frappe
import frappe.sessions
import frappe.utils

def get_context(context):
    # Check if the user is logged in
    if frappe.session.user == "Guest":
        # Redirect to login if not logged in
        frappe.local.flags.redirect_location = "/login?redirect-to=/flight-booking"
        raise frappe.Redirect

    # Check if the user has permission to book a ticket
    allowed_roles = ["Travel Agent", "Ticket Manager"]
    user_roles = frappe.get_roles()

    # Remove print statement in production
    print(allowed_roles, user_roles, "hello from line 18", frappe.utils.now_datetime())

    isRoleMatch = False

    for roleAllowed in allowed_roles:
        if isRoleMatch==True:
            break
        for haveRole in user_roles:
            
            if roleAllowed == haveRole:
                isRoleMatch = True
                break

    if not isRoleMatch:
        frappe.throw("You are not authorized to book a ticket.", frappe.PermissionError)

    # Retrieve CSRF token
    context.csrf = frappe.sessions.get_csrf_token()
    # Retrieve flight name from request parameters
    context.flightName = frappe.form_dict.get("flight")
    return context
