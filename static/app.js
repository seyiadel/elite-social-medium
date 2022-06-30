let overlay = document.querySelector('.overlay')
let hamburger = document.querySelector('.hamburger-icon')
let addPost = document.querySelectorAll('.addPost')
let content = document.querySelector('.posts')
let menuList = document.querySelector('.mobile_menu_list')
let mobileClose = document.querySelectorAll(".mobile_menu_list_lists_para")
const image_input = document.querySelector("#image-input");
let close = document.querySelector('.close')

for(let add of addPost){
  add.addEventListener('click', () => {
    overlay.style.width = '100%'
})
}

hamburger.addEventListener('click', () => {
  menuList.style.display = 'block'
})
content.addEventListener('click', () => {
  menuList.style.display = 'none'
})
for (let mobile of mobileClose){
  mobile.addEventListener('click', () => {
    menuList.style.display = 'none'
  })
}

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