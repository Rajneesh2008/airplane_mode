// Copyright (c) 2024, Rajneesh yadav and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
  refresh(frm) {
      if(!frm.doc?.is_leach){

        if(frm.doc?.tenant){
          frm.set_value("is_leach",1)
          frm.save()
        }

      }
      // Fetch all Shop records to calculate total and available shops
      frappe.call({
          method: "frappe.client.get_list",
          args: {
              doctype: "Shop",
              fields: ["name", "status"]
          },
          callback: function(response) {
              if(response.message) {
                  let total_shops = response.message.length;
                  let available_shops = response.message.filter(shop => shop.status === "Available").length;

                  // Set the values in the form fields
                  frm.set_value('total_shop', total_shops);
                  frm.set_value('available_shop', available_shops);

                  frm.refresh_field('total_shop');
                  frm.refresh_field('available_shop');
              }
          }
      });
  },

  // Trigger whenever the 'status' field is changed
  status(frm) {
      frappe.call({
          method: "frappe.client.get_list",
          args: {
              doctype: "Shop",
              fields: ["name", "status"]
          },
          callback: function(response) {
              if(response.message) {
                  let total_shops = response.message.length;
                  let available_shops = response.message.filter(shop => shop.status === "Available").length;

                  // Update the available_shop and total_shop fields
                  frm.set_value('total_shop', total_shops);
                  frm.set_value('available_shop', available_shops);

                  frm.refresh_field('total_shop');
                  frm.refresh_field('available_shop');
              }
          }
      });
  },

 
});

