const addBtn = document.querySelector('.add-button');
const customerInfo = document.querySelectorAll('.customer-info');          
console.log(addBtn)
addBtn.addEventListener('click',(e)=>{
    document.querySelectorAll('.error-message').forEach(error=> error.remove());
    customerInfo.forEach(element => {
        const newElement = document.createElement('div');
        newElement.classList.add('error-message');
        newElement.textContent = "This field is required!";
        if(element.value === ""){
            e.preventDefault();
            element.parentElement.insertBefore(newElement, element);
            element.style.outline = "1px solid red";

        }
    })
})


