import frappe
from frappe.utils import add_days, today


def send_test_email():

    try:
        frappe.sendmail(
            recipients="rajneeshyadav1107@gmail.com",
            subject="Test Email from Frappe",
            message="This is a test email to verify SMTP configuration in Frappe.",
            delayed=False
        )
        frappe.msgprint("Test email sent successfully!")
    except Exception as e:
        print(f"Failed to send test email: {e}")  # This will help you see the error in the console.
        frappe.msgprint(f"Failed to send test email: {e}")

import frappe
from frappe.utils import today, add_days

def notify_contract_end():
    # Fetch contracts expiring within the next 7 days
    print("Fetching contracts expiring in the next 7 days...")
    contracts = frappe.get_all(
        "Lease Contract",
        filters={
            "contract_expiry_date": ["between", [today(), add_days(today(), 7)]]
        },
        fields=["tenant", "shop", "contract_expiry_date"]
    )

    # Check if any contracts were found
    if not contracts:
        print("No contracts expiring in the next 7 days.")
        return

    print(f"Found {len(contracts)} contracts expiring soon.")
    for contract in contracts:
        print(f"Processing contract: {contract}")

        # Get tenant's email
        tenant_email = frappe.db.get_value("Tenant", contract.tenant, "email")
        shop_name = frappe.db.get_value("Shop", contract.shop, "shop_name")

        if tenant_email:
            # Send reminder email
            frappe.sendmail(
                recipients=[tenant_email],
                subject="Shop Contract Ending Soon",
                message=(
                    f"Dear Tenant,\n\n"
                    f"Your contract for the shop '{shop_name}' will expire on "
                    f"{contract.contract_expiry_date}. Please contact us if you "
                    f"wish to renew it.\n\nThank you."
                ),
                delayed=False
            )
            print(f"Email sent successfully to {tenant_email}.")
        else:
            print(f"No email found for tenant: {contract.tenant}.")
