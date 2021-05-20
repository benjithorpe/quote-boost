let quoteCategories = document.getElementById('tags');
let quoteContent = document.getElementById('content');
let quoteAuthor = document.getElementById('author');
const nextBtn = document.getElementById('nextBtn');
const quotesAPI = "https://api.quotable.io/random";


nextBtn.addEventListener('click', () => {
  fetch(quotesAPI)
    .then((response) => response.json())
    .then((data) => {
      quoteContent.innerText = data['content'];
      quoteCategories.innerText = data['tags'].join(', ');
      quoteAuthor.innerText = data['author'];
    })
    .catch((error) => console.log("ERROR: -> ", error))
});
