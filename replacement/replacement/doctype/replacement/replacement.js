frappe.ui.form.on('Replacement', {
    before_save: function(frm) {
        frappe.call({
            method: 'replacement.replacement.test.create_reverse_replacement_doc',
            args: {
                item: frm.doc.item,
                replacement_item: frm.doc.replacement_item
            },
            callback: function(r) {
                if (!r.exc) {
                    // Handle the response if needed
                }
            }
        });
    },
    
    refresh: function(frm) {
        // Add custom button to the toolbar
        frm.add_custom_button(__('Search Item'), function() {
            frappe.prompt([
                {
                    'fieldname': 'item',
                    'fieldtype': 'Link',
                    'label': __('Item'),
                    'options': 'Item',
                    'reqd': 1,
                },
            ], function(values){
                frappe.call({
                    method: 'replacement.replacement.need.search_and_replace',
                    args: {
                        item_code: values.item // Ensure the correct argument name
                    },
                    callback: function(r) {
                        if (!r.exc) {
                            // Create a table to display search results
                            var table = '<table class="table table-bordered">';
                            table += '<thead><tr><th class="column1">Replacements for ' + values.item + '</th><th class="column2">Item Name</th></tr></thead>';
                            table += '<tbody>';
                            
                            // Iterate through replacements and add a row for each
                            for (var replacement in r.message.combined_list) {
                                table += '<tr>';
                                table += '<td class="column1">' + replacement + '</td>';
                                table += '<td class="column2">' + r.message.combined_list[replacement] + '</td>';
                                table += '</tr>';
                            }
                            
                            table += '</tbody></table>';
                            
                            // Display the table in a dialog
                            frappe.msgprint({
                                message: table,
                                title: __('Search Results'),
                                wide: true
                            });
                        }
                    }
                });
            }, __('Search Item'), 'View');
        });
    }
});
