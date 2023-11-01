$(document).ready(function() {
    const hello = $("#hello");

    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        const translate = data.hello;
        hello.text(translate);
    });
});