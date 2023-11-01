$(document).ready(function() {
    const addItem = $("#add_item");

    addItem.click(function() {
        const newItem = $("<li>Item</li>");

        $(".my_list").append(newItem);
    });
});