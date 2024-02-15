const dropDownItems = document.querySelectorAll('.dropdown-menu');
let activeItem = null;

//check sessionstorage for the active item on page load

const storedActiveItemIndex = sessionStorage.getItem('activeItemIndex');

if(storedActiveItemIndex !== null){
    activeItem = dropDownItems[parseInt(storedActiveItemIndex, 10)]
    showDropdown(activeItem);
}

dropDownItems.forEach((item, index)=>{
    item.addEventListener('click',(e)=>{
        const element = item.lastElementChild;
        if(e.currentTarget === activeItem){
           
            hideDropdown(element);
            activeItem = null;
            
        }
        else{
            if(activeItem){
          
                hideDropdown(activeItem.lastElementChild)
            }
         
            showDropdown(item)
            activeItem = e.currentTarget;
            sessionStorage.setItem('activeItemIndex',index.toString());
        }
    })
})


function showDropdown(item){
    const element = item.lastElementChild;
    element.style.display = 'block';
}


function hideDropdown(element){
    element.style.display= 'none';
}



// admin hamburger
const leftContainer = document.querySelector('.left-container')
const hamburger = document.getElementById('hamburger-icon')
let is_clicked = false;
hamburger.addEventListener('click', (e)=>{
    if (!is_clicked){
        leftContainer.style.display = 'block';
        document.body.style.overflow = 'hidden';
        hamburger.children[0].classList.add('fa-xmark')
        hamburger.children[0].classList.remove('fa-bars')
        hamburger.style.color= 'red';
    }
    else{
        leftContainer.style.display = 'none';
        document.body.style.overflow = 'auto';
        hamburger.children[0].classList.add('fa-bars')
        hamburger.children[0].classList.remove('fa-xmark')
        hamburger.style.color= 'white';

    }
    is_clicked = !is_clicked;

})