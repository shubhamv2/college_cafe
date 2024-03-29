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
        e.target.parentElement.style.outline="1px solid rgb(0,185,0)"
    });
    inputTag.addEventListener('blur',(e)=>{
        e.target.parentElement.style.outline="";
    })
})



const submitBtn = document.getElementById('submit-btn')
submitBtn.addEventListener('click',(e)=>{
    document.querySelectorAll('.error-message').forEach(error=> error.remove());
    inputTags.forEach(element =>{
        const newElement = document.createElement('div');
        newElement.textContent = "This is required!";
        newElement.classList.add('error-message');
        if(element.value === ""){
            e.preventDefault();
            element.parentElement.style.outline = "1px solid red";
            element.parentElement.parentElement.insertBefore(newElement, element.parentElement)
        }
    })
    
})