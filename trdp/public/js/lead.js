frappe.ui.form.on("Lead",{
    refresh(frm){
        frm.add_custom_button("My Opportunity",function(){
            frappe.new_doc("Opportunity",{
            party_name:frm.doc.name,
            contact_person:frm.doc.first_name,
            job_title:frm.doc.job_title

            })
           

        })
    }
})