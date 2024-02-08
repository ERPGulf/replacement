frappe.pages['search-replacement'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Search Replacement',
        single_column: true
    });

    var field = page.add_field({
        fieldname: 'item',
        fieldtype: 'Link',
        label: __('Search Item'),
        options: 'Item',
        reqd: 1,
        input_css: {
            'width': '320%',
            'margin-bottom': '10px',
            'padding': '20px',
            'border-radius': '8px',
            'border': '1px solid #666'
        }
    });

    var $container = $('<div class="search-container"></div>').appendTo(page.body);

    var $searchButton = $('<button class="btn btn-primary btn-lg">View</button>').appendTo($container); // Added 'btn-lg' class to make the button slightly larger

    var $searchResultsContainer = $('<div class="search-results"></div>').appendTo(page.body);

    $searchButton.on('click', function() {
        var item = field.get_value();
        if (item) {
            frappe.call({
                method: 'replacement.replacement.need.search_and_replace',
                args: {
                    item_code: item
                },
                callback: function(r) {
                    if (!r.exc) {
                        if (Object.keys(r.message.combined_list).length > 0) {
                            var table = '<table class="table table-bordered table-sm" style="max-width: 50%; border-color: #111; border-width: 2px;">'; // Added border-width style
                            table += '<thead><tr><th style="width: 50%; border-color: #111; border-width: 2px; text-align: center;">Replacements for ' + item + '</th><th style="width: 50%; border-color: #111; border-width: 2px; text-align: center;">Name</th></tr></thead>'; // Added width style for equal column size and border-width and text-align style for header cells
                            table += '<tbody>';

                            $.each(r.message.combined_list, function(replacement_item, replacement_name) {
                                table += '<tr><td style="width: 50%; border-color: #111; border-width: 2px; color: #111; text-align: center;">' + replacement_item + '</td><td style="width: 50%; border-color: #111; border-width: 2px; color: #111; text-align: center;">' + replacement_name + '</td></tr>';
                            });

                            table += '</tbody></table>';

                            $searchResultsContainer.html(table);
                        } else {
                            $searchResultsContainer.html('<p>No replacement items found.</p>');
                        }
                    }
                }
            });
        }
    });

    $container.css({
        'display': 'flex',
        'justify-content': 'center',
        'margin-top': '10px'
    });

    field.$wrapper.css({
        'margin-right': '10px'
    });

    $searchResultsContainer.css({
        'display': 'flex',
        'justify-content': 'center',
        'margin-top': '20px'
    });

    $searchButton.css({
        'background-color': '#337ab7',
        'border-color': '#337ab7'
    });
}
