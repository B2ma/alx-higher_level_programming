$(document).ready(function () {
  // Make an AJAX request to fetch data from the SWAPI API
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract the array of movies from the fetched data
    const movies = data.results;

    // Iterate through the movies and append titles to the <ul id="list_movies">
    movies.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
