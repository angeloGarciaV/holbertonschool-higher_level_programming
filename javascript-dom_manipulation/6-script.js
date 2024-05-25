const character = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(response => response.json())
.then(data =>{
  console.log(data)
  character.innerText = data.name;
});