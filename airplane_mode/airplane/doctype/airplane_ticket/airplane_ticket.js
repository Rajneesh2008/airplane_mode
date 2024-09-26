// Copyright (c) 2024, Rajneesh yadav and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
    frm.add_custom_button("Assign Seats",()=>{
      let d = new frappe.ui.Dialog({
        title: 'Select Seat',
        fields: [
            {
                label: 'Seat Number',
                fieldname: 'seats',
                fieldtype: 'Data'
            }
        ],
        size: 'small', // small, large, extra-large 
        primary_action_label: 'Assign',
        primary_action(values) {
          frm.set_value("seats",values.seats)
          frm.save()
          d.hide();
        }
    });
    
    d.show();
    
    },"Actions")
	},
});

frappe.ui.form.on("Airplane Ticket", {
  refresh(frm) {

	}
});

frappe.ui.form.on("Airplane Ticket Add-on Item", {
  
  amount(frm,cdt,cdn){
    let totalAmout = 0
    for(let items in frm.doc.add_ons){
      totalAmout+=items.amount
    }
    if(totalAmout){
      totalAmout+=frm.doc.flight_price;
  
      frm.set_value("total_amount",totalAmout)
      frm.save()
    }
    }
});




