$(document).ready(function() {
    const updateHeader = $("#update_header");

    updateHeader.click(function() {
        const header = $("header");
        header.text("New Header!!!");
    });
});