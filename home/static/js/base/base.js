// Function for fixing navbar at top
function navbarfix() {

    window.onscroll = function () { myFunction() };
  
    let navbar = document.querySelector(".navbar-wrapper");
  
    function myFunction() {
      if (window.scrollY > 0) {
        navbar.classList.add("fixed");
      } else {
        navbar.classList.remove("fixed");
      }
    }
  
  }
  
  
  
  
  
  
  function userProfileDetails(){
    // let isPopup = false;
    const user = document.querySelector('.user-png-icon');
    const close = document.querySelector('.close-popup');
    const userPopup = document.querySelector('.user-popup');
    user.addEventListener('click',(e)=>{
      userPopup.style.display = "block"; 
    })
  
    close.addEventListener('click',(e)=>{
      userPopup.style.display = "none"; 
    })
  
  }
  
  function editUserDetails(mypara){
    const editIcons = document.querySelectorAll('.edit-icon')
    const ItemToEdit = document.getElementById(mypara);
    editIcons.forEach((element,index)=>{
      element.addEventListener('click',(e)=>{
        if(ItemToEdit.readOnly){
          ItemToEdit.removeAttribute('readonly')
          ItemToEdit.focus()
        }
      })
    })
  }
  
  userProfileDetails();
  navbarfix();
  