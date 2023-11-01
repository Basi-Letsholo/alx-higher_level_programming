$(document).ready(function() {
    const toggleHeader = $("#toggle_header");

    toggleHeader.click(function() {
        const header = $("header");

        if (header.hasClass("red")) {
            header.removeClass("red").addClass("green");
        } else {
            header.removeClass("green").addClass("red");
        }
    });
});