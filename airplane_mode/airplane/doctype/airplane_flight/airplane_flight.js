// Copyright (c) 2024, Rajneesh yadav and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	// refresh(frm) {

	// },
  onload:function(frm){
    
    if(frappe.user.has_role("Travel Agent")){
      frm.set_df_property('crew_members', 'hidden', true);
    }else{
      frm.set_df_property('crew_members', 'hidden', false);
    }

  }
});
