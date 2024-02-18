const submitBtn = document.querySelector('.submit-btn');
const changeItemContainer = document.querySelectorAll('.change-item-container input');
const changeDetailsHeading = document.querySelector('.changedetails-heading');
const changeForm = document.querySelector('.change-details');
let newElement = document.createElement('div');
newElement.textContent = 'At least one field should be filled!';
let isAllBlank = true;
newElement.classList.add('error-message')
submitBtn.addEventListener('click', (e)=>{
    changeItemContainer.forEach((element)=>{
        element.value !== ""? isAllBlank = false :null;
    })
    if(isAllBlank){
        e.preventDefault();
        changeDetailsHeading.insertAdjacentElement('afterend', newElement)

    }
})

contactFormValidator()





