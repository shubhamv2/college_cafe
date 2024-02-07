const inputTags = document.querySelectorAll('.input-tag');
inputTags.forEach((inputTag)=>{ 
    inputTag.addEventListener('focus',(e)=>{
        e.target.style.outline="1px solid black"
    });
    inputTag.addEventListener('blur',(e)=>{
        e.target.style.outline="";
    })
})