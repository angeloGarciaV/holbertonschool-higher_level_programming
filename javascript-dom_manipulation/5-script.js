const myHeader = document.querySelector('header');
const updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', ()=>{
  myHeader.innerText = 'New Header!!!';
});