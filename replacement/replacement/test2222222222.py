import frappe
frappe.init(site="rowad.baraktain.com")
frappe.connect()


from frappe import _

def apply_pricing_rule(item_code, patient_encounter):
    # Get the Pricing Rule for the given item_code
    pricing_rule = frappe.get_doc("Pricing Rule", {"item_code": item_code})
    
    # If pricing_rule exists and it has a discount_amount
    if pricing_rule and pricing_rule.discount_amount:
        # Get the rate of the item
        item = frappe.get_doc("Item", item_code)
        item_rate = item.rate
        
        # Calculate the new rate with discount applied
        discounted_rate = item_rate - pricing_rule.discount_amount
        
        # Save the discounted rate in the Patient Encounter
        patient_encounter.rate = discounted_rate
        patient_encounter.save()
    else:
        frappe.msgprint(_("No pricing rule found for this item."))

# Usage example:
# Assuming patient_encounter is the instance of Patient Encounter document and item_code is the item code being checked
apply_pricing_rule(item_code, patient_encounter)
