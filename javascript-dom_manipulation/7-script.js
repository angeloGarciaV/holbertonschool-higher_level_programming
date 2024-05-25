const listMovies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
  data.results.forEach(movie => {
    const movieTitle = document.createElement('li');
    movieTitle.innerText = movie.title;
    listMovies.appendChild(movieTitle);
  })
})