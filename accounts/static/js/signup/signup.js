const inputTags = document.querySelectorAll('.input-tag');
inputTags.forEach((inputTag)=>{ 
    inputTag.addEventListener('focus',(e)=>{
        e.target.style.outline="1px solid rgb(0, 185,0)"
    });
    inputTag.addEventListener('blur',(e)=>{
        e.target.style.outline="";
    })
})




const submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click',(e)=>{
    document.querySelectorAll('.error-message').forEach((error)=> error.remove());

    inputTags.forEach(element=>{
        let newElement = document.createElement('div')
        newElement.classList.add('error-message');
        newElement.textContent = "This field is required!"
        if(element.value ===""){
            e.preventDefault();
            element.parentElement.insertBefore(newElement, element)
            element.style.outline = "1px solid red"

        }

    })

})