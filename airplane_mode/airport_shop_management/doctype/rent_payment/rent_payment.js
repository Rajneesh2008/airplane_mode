// Copyright (c) 2024, Rajneesh yadav and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Payment", {
	refresh(frm) {
    console.log(frm.doc)
      if(frm.doc?.shop){
       frappe.db.get_doc('Shop', frm.doc.shop)
        .then(doc => {
            console.log(doc)
            frm.doc.tenant = doc.tenant
            frm.save()
        })
      }

	},
});
