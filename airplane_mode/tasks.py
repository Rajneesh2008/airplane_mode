import frappe
from frappe.utils import add_days, today


def run_test1():
    print("Hi test")


def send_test_email(recipient_email):
    print("Hello test")
    try:
        frappe.sendmail(
            recipients=recipient_email,
            subject="Test Email from Frappe",
            message="This is a test email to verify SMTP configuration in Frappe."
        )
        print("Email send ")
        frappe.msgprint("Test email sent successfully!")
    except Exception as e:
        print(f"Failed to send test email: {e}")  # This will help you see the error in the console.
        frappe.msgprint(f"Failed to send test email: {e}")

def notify_contract_end():
    # Fetch contracts expiring in the next 7 days
    contracts = frappe.get_all(
        "Lease Contract",
        filters={"contract_expiry_date": add_days(today(), 7)},
        fields=["tenant", "shop"]
    )

    for contract in contracts:
        tenant_email = frappe.db.get_value("Tenant", contract.tenant, "email")  # Get tenant's email
        shop_name = frappe.db.get_value("Shop", contract.shop, "shop_name")  # Get shop name
        
        if tenant_email:
            frappe.sendmail(
                recipients=tenant_email,
                subject="Shop Contract Ending Soon",
                message=f"Your contract for the shop '{shop_name}' will expire in 7 days. Please contact us if you need to renew it."
            )


def create_monthly_rent_reminder():
    tenants = frappe.get_all("Tenant", fields=["tenant_name", "email"])

    for tenant in tenants:
        # Create an Event in Frappe to remind tenants about rent
        event = frappe.get_doc({
            "doctype": "Event",
            "subject": "Monthly Rent Payment Reminder",
            "description": f"Reminder for {tenant.name} to pay rent for the current month.",
            "event_type": "Private",
            "starts_on": today(),
            "all_day": 1,
            "owner": tenant.email
        })
        event.insert(ignore_permissions=True)
