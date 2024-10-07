# color template for styling...
# https://icolorpalette.com/imagepalette/color-palette-ideas-from-sky-airline-airplane-image

# svg icon website
#https://svgsilh.com/tag/airplane-2.html


# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE


import frappe

def get_context(context):
    # take out filters query from the request
    status = frappe.form_dict.get('status')
    min_rent = frappe.form_dict.get('min_rent')
    max_rent = frappe.form_dict.get('max_rent')

    #store the  filters quiery in object
    filters = {}

    if status:
        filters['status'] = status
    if min_rent and max_rent:
        filters['rent_amount'] = ['between', [float(min_rent), float(max_rent)]]
    elif min_rent:
        filters['rent_amount'] = ['>=', float(min_rent)]
    elif max_rent:
        filters['rent_amount'] = ['<=', float(max_rent)]

    # Fetch  all filtered shops
    shops = frappe.get_list('Shop',
                            filters=filters,
                            fields=['name','shop_name', 'shop_number', 'status', 'rent_amount', 'tenant', 'contract_start_date', 'contract_expiry_date'])

    # Add shops to the context
    context.shops = shops
    context.status_filter = status
    context.min_rent_filter = min_rent
    context.max_rent_filter = max_rent

    return context
