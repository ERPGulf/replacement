import frappe

# frappe.init(site="husna.erpgulf.com")
# frappe.connect()
@frappe.whitelist(allow_guest=True)
def search_and_replace(item_code, all_replacements=None):
    if all_replacements is None:
        all_replacements = set()

    replacements = frappe.get_all('Replacement', filters={'item': item_code}, fields=['replacement_item'])
    replacements = {replacement.get('replacement_item') for replacement in replacements}

    for replacement in replacements:
        if replacement not in all_replacements:
            all_replacements.add(replacement)
            # Recursive call to include replacements of replacements
            search_and_replace(replacement, all_replacements)

    # Construct the combined list excluding the original item code
    combined_list = {replacement: frappe.get_value("Item", replacement, "item_name") for replacement in all_replacements if replacement != item_code}

    return {'combined_list': combined_list}

