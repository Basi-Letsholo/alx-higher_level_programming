$(document).ready(function() {
    const redHeader = $("#red_header");

    redHeader.click(function() {
        const header = $("header");
        header.css("color", "#FF0000");
    });
});