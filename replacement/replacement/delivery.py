import frappe
# frappe.init(site="husna.erpgulf.com")
# frappe.connect()
import sys
from frappe import _
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def validate_returned_quantity(doc_name):
    try:
        doc = frappe.get_doc('Delivery Note', doc_name)
        differences = {}

        # Validate quantity for each item
        for item in doc.items:
            difference = validate_item_quantity(item, doc)
            differences[item.name] = difference
        has_zero_difference = any(difference == 0 for difference in differences.values())

        if has_zero_difference:
            # Set the document status to 'Closed'
            frappe.db.set_value('Delivery Note', doc_name, 'status', 'Closed')
        return differences
    except frappe.DoesNotExistError:
        frappe.msgprint(_("Delivery Note not found: {0}").format(doc_name))
    except Exception as e:
        frappe.msgprint(str(e))

def validate_item_quantity(item, delivery_note_doc):
    original_qty = abs(item.get('qty', 0))
    returned_qty = abs(item.get('returned_qty', 0))
    sales_invoice_return_qty = 0
    
    sales_invoice_name = frappe.get_value('Sales Invoice Item', {'delivery_note': delivery_note_doc.name}, 'parent')

    qty_in_invoice = 0

    if sales_invoice_name:
        sales_invoice_doc = frappe.get_doc('Sales Invoice', sales_invoice_name)
        for item in sales_invoice_doc.items:
            sales_invoice_return_qty = abs(item.get('qty', 0))

        original_sales_invoice_note = sales_invoice_doc.get('return_against')
        if original_sales_invoice_note:
            original_sales_invoice_doc = frappe.get_doc('Sales Invoice', original_sales_invoice_note)
            for invoice_item in original_sales_invoice_doc.items:
                qty_in_invoice = invoice_item.qty
        else:
            print("No linked Sales Invoice found for the given Delivery Note.")
            pass 
    else:
        pass

    difference = (original_qty - returned_qty) - qty_in_invoice

    item.difference = difference
    return difference
   
import frappe
# frappe.init(site="hoda-dev.erpgulf.com")
# frappe.connect()


@frappe.whitelist(allow_guest=True)
def calculate_item_quantities(item_code):
    try:
      
        delivery_note_qty = frappe.get_all("Delivery Note Item", pluck="qty", filters={"name": item_code, "docstatus": 1})
        returned_delivery_qty = frappe.get_all("Delivery Note Item", pluck="qty", filters={"dn_detail": item_code, "docstatus": 1})
        invoice_qty = frappe.get_all("Sales Invoice Item", pluck="qty", filters={"dn_detail": item_code, "docstatus": 1})

        # Calculate total quantities
        total_delivery_note_qty = sum(delivery_note_qty)
        total_returned_deliverynote_qty = sum(returned_delivery_qty)
        total_invoice_qty = sum(invoice_qty)

        # Calculate result
        result = (total_delivery_note_qty + total_returned_deliverynote_qty ) - total_invoice_qty

        return {
            "doqty": total_delivery_note_qty,
            "retqty": total_returned_deliverynote_qty,
            "invqty": total_invoice_qty,
            "result": result
        }
    except Exception as e:
        # Handle exceptions here
        return {"error": str(e)}


import frappe
# frappe.init(site="husna.erpgulf.com")
# frappe.connect()
import sys
from frappe import _

def validate_status_quantity(doc, method):
    try:
        for item in doc.items:
            validate_status(item, doc)
    except Exception as e:
        frappe.msgprint(str(e))


def validate_status(item, delivery_note_doc):
    original_qty = abs(item.get('qty', 0))
    returned_qty = abs(item.get('returned_qty', 0))

    # frappe.msgprint(f"Original Qty: {original_qty}, Returned Qty: {returned_qty}")

    sales_invoice_name = frappe.get_value('Sales Invoice Item', {'delivery_note': delivery_note_doc.name}, 'parent')

    if sales_invoice_name:
        sales_invoice_doc = frappe.get_doc('Sales Invoice', sales_invoice_name)
        original_sales_invoice_note = sales_invoice_doc.get('return_against')

        if original_sales_invoice_note:
            original_sales_invoice_doc = frappe.get_doc('Sales Invoice', original_sales_invoice_note)
            # frappe.msgprint(f"Original sales invoice doc is: {original_sales_invoice_doc}")
            for invoice_item in original_sales_invoice_doc.items:
                qty_in_invoice = invoice_item.qty
                # print(f"Quantity in Sales Invoice for item {invoice_item.item_code}: {qty_in_invoice}")
        else:
            frappe.msgprint("No linked Delivery Note found in Sales Invoice.")
    else:
        frappe.msgprint("No linked Sales Invoice found for the given Delivery Note.")

    difference = (original_qty - returned_qty) - qty_in_invoice
    item.difference = difference

    if difference == 0:
        delivery_note_doc.db_set('status', 'Closed', commit=True, update_modified=True)