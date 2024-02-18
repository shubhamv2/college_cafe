function contactFromValidation() {
    const formBtn = document.querySelector('.form-btn')
    const contactInputFields = document.querySelectorAll('.form-items .contact-input');
    const handleClick = (e)=>{
        document.querySelectorAll('.submit-error').forEach(error => error.remove());    
        contactInputFields.forEach(element => {
            let newElement = document.createElement('div')
            newElement.textContent = 'This field is required!';
            newElement.classList.add('submit-error')
            if (element.value.trim() === '') {
                e.preventDefault()
                element.style.border = '1px solid red';
                element.parentElement.insertBefore(newElement, element)
            }
        })

    }
    formBtn.addEventListener('click', handleClick)

}

contactFromValidation();