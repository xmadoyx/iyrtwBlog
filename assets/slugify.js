const titleInput = document.querySelector('input[name=title]')
// querySelector gets elements from our document(=html page)
// the input of querySelector is names equaled to title here
const slugInput = document.querySelector('input[name=slug]')
// the input of querySelector is names equaled to title here

const slugify = (val)=>{
  return val.toString().trim()
    // slugifying the names word by word
    .replace(/&/g, '-and-')
    // replace & with -and-
    // 'g' is used to find all the occurrences of the pattern instead of stopping after the first match
    .replace(/[\s\W-]+/g, '-')
    // replace spaces and non-word chars with -
};

titleInput.addEventListener('keyup', (e)=>{
  slugInput.setAttribute('value',slugify(titleInput.value))
});
// event listener for titleInput, that when we type sth in title, event listener receives that text and passes it to slugify function eventually
