let overlay = document.querySelector('.overlay')
let addPost = document.querySelector('.addPost')
const image_input = document.querySelector("#image-input");
let close = document.querySelector('.close')

addPost.addEventListener('click', () => {
    overlay.style.width = '100%'
})

close.addEventListener('click', () => {
    overlay.style.width = '0%'
})

image_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      const uploaded_image = reader.result;
      document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
    });
    reader.readAsDataURL(this.files[0]);
  });