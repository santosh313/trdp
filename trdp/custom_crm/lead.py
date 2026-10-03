import frappe

@frappe.whitelist()
def create_opportunity(lead_name):
    """
    Create an Opportunity from a Lead.
    """
    lead = frappe.get_doc("Lead", lead_name)
    opportunity = frappe.new_doc("Opportunity")
    
    opportunity.lead_name = lead.name
    opportunity.customer_name = lead.company_name
    opportunity.contact_person = lead.contact_person
    opportunity.email_id = lead.email_id
    opportunity.phone = lead.phone
    opportunity.status = "Open"
    
    # Save the Opportunity
    opportunity.insert()
    
    # Optionally, you can update the Lead status to indicate that an Opportunity has been created
    
    return opportunity.name

import requests

@frappe.whitelist()
def get_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    posts = response.json()

    created = 0
    skipped = 0

    for post in posts:
        if frappe.db.exists("Lead", {"custom_lead_id": post.get("id")}):
            skipped += 1
            continue

        lead = frappe.new_doc("Lead")
        lead.custom_lead_id = str(post.get("id"))   
        lead.first_name = str(post.get("id"))        
        lead.job_title = post.get("title")           
        lead.insert(ignore_permissions=True)
        created += 1

    frappe.db.commit()
    return {"created": created, "skipped": skipped, "total_fetched": len(posts)}