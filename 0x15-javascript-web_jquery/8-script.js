$(document).ready(function() {
    const movieList = $("#list_movies");

    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        const movies = data.results;

        $.each(movies, function(index, movie) {
            movieList.append("<li>" + movie.title + "</li>");
        });
    });
});