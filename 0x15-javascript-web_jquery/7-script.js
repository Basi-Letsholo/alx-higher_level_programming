$(document).ready(function() {
    const character = $("#character");

    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
        const charName = data.name;
        character.text("Character Name: " + charName);
    });
});