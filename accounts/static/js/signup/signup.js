const inputTags = document.querySelectorAll('.input-tag');
inputTags.forEach((inputTag)=>{ 
    inputTag.addEventListener('focus',(e)=>{
        e.target.style.outline="1px solid rgb(0, 185,0)"
    });
    inputTag.addEventListener('blur',(e)=>{
        e.target.style.outline="";
    })
})