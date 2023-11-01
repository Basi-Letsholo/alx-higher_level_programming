$(document).ready(function() {

    $("#add_item").click(function() {
        const newItem = $("<li>Item</li>");
        $(".my_list").append(newItem);
    });

    $("#remove_item").click(function() {
        const listItems = $(".my_list li");
        if (listItems.length > 0) {
            listItems.last().remove();
        }
    });

    $("#clear_list").click(function() {
        $(".my_list").empty();
    });
});