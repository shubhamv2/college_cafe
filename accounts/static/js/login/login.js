//password visible icon
const passowrdIcon = document.getElementById("password-icon");
let isVisible = false;
window.addEventListener("DOMContentLoaded",(e)=>{
    passowrdIcon.innerHTML=`<i class="fa-regular fa-eye" id="eye-show"></i>`;
    isVisible = !isVisible;
})

passowrdIcon.addEventListener("click",(e)=>{
    const passwordField = document.getElementById('password-field');
    if(isVisible){
        passowrdIcon.innerHTML=`<i class="fa-regular fa-eye-slash" id="eye-slash"></i>`;
        passwordField.type = "text";
    }
    else{
        passowrdIcon.innerHTML=`<i class="fa-regular fa-eye" id="eye-show"></i>`;
        passwordField.type = "password";
    }
    isVisible=!isVisible;
})


const inputTags = document.querySelectorAll('.input-tags');
inputTags.forEach((inputTag)=>{ 
    inputTag.addEventListener('focus',(e)=>{
        e.target.parentElement.style.outline="1px solid black"
    });
    inputTag.addEventListener('blur',(e)=>{
        e.target.parentElement.style.outline="";
    })
})