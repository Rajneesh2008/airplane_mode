
#  import  important packages
import frappe
from frappe import _,sendmail
from frappe.auth import LoginManager
from frappe.utils import random_string

# function for creating a ticket------------------------------------------------------
@frappe.whitelist()
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
    })
    new_ticket.insert()
    frappe.db.commit()
    return {"status": "success", "message": "Ticket booked",
            "flight":flight_name,
            "passenger":passenger_name,
            "departure_date":flight_doc.date_of_departure
            }




# register a new user--------------------------------------------------
@frappe.whitelist(allow_guest=True)
def register(email, password, fullName):
    print(email, password, fullName)
    if frappe.db.exists("User", {"email": email}):
        return {"msg": "User is already Registered", "status": "Failed"}
    
    token = random_string(32)
    frappe.cache().set_value(token, {
        "email": email,
        "password": password,
        "full_name": fullName
    }, expires_in_sec=600)  # Token expires in 10 minutes
    
    verification_link = f"{frappe.utils.get_url()}/api/method/airplane_mode.api.verify_email?token={token}"
    send_verification_email(fullName, email, verification_link)
    
    return {"msg": "A verification email has been sent to your email address. Please verify to complete registration.", "status": "Success"}

#  send a verification email to user email account
def send_verification_email(fullName, email, verification_link):
    subject = _("Verify Your Email Address")
    message = f"""
    <h3>Hello {fullName},</h3>
    <p>Please click on the link below to verify your email address and complete your registration:</p>
    <a href="{verification_link}">Verify Email</a>
    <p>Best regards,<br>Airplane_mode Team</p>
    """
    frappe.sendmail(
        recipients=email,
        subject=subject,
        message=message,
        delayed=False
    )

# as user will clicked on link it will save the data to db
@frappe.whitelist(allow_guest=True)
def verify_email(token):
    data = frappe.cache().get_value(token)
    
    if not data:
        return {"msg": "Invalid or expired verification token.", "status": "Failed"}
    
    user = frappe.get_doc({
        "doctype": "User",
        "email": data["email"],
        "first_name": data["full_name"],
        "new_password": data["password"],
        "enabled": 1
    })
    user.insert()
    frappe.db.commit()
    
    frappe.cache().delete_value(token)
    
    return {"msg": "Email verified successfully. You can now log in.", "status": "Success"}


# login function with user-email and password--------------------------------------------------------
@frappe.whitelist(allow_guest=True)
def login(email, password):
    try:
        if email and password:
            frappe.local.login_manager = LoginManager()
            frappe.local.login_manager.authenticate(user=email, pwd=password)
            frappe.local.login_manager.post_login()
            return {"status": "success", "msg": _("Login Successful")}
        else:
            return {"status": "error", "msg": _("Invalid credentials")}

    except frappe.exceptions.AuthenticationError:
        # Handle authentication failure specifically
        return {"status": "error", "msg": _("Invalid username or password")}

    except Exception as e:
        # Log the exception for debugging purposes
        frappe.log_error(frappe.get_traceback(), _("Login Error"))
        return {"status": "error", "msg": _("An unexpected error occurred. Please try again.")}
