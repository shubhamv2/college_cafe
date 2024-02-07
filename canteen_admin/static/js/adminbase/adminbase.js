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
            // element.style.display = "none";
            hideDropdown(element);
            activeItem = null;
            // localStorage.removeItem('activeItemIndex');
        }
        else{
            if(activeItem){
                // activeItem.lastElementChild.style.display = 'none';
                hideDropdown(activeItem.lastElementChild)
            }
            // element.style.display = "block";
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