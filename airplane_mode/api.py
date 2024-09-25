
import frappe

@frappe.whitelist()

def getUser():
  return {
    "name":"Rajneesh",
    "gender":"Male",
    "age":54
  }