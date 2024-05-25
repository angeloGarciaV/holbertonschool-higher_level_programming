const addItem = document.getElementById('add_item');
const myList = document.getElementsByClassName('my_list');

addItem.addEventListener('click', ()=>{
  const listItem = document.createElement('li');
  listItem.innerText = 'Item';
  myList[0].appendChild(listItem);
});