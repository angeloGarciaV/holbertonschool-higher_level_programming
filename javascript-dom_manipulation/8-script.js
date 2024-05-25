const translate = new Promise((resolve, reject) => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const hello = document.getElementById('hello');
      hello.innerText = data.hello;
      resolve(data);
    })
    .catch(error => {
      console.error('Error:', error);
      reject(error);
    });
});