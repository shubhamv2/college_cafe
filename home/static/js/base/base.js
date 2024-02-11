// 
// Function for fixing navbar at top
function userProfileDetails() {
  const user = document.querySelector('.user-png-icon');
  const close = document.querySelector('.close-popup');
  const userPopup = document.querySelector('.user-popup');
  user.addEventListener('click', (e) => {
    userPopup.style.display = "block";
    document.body.style.overflow = 'hidden';

  })

  close.addEventListener('click', (e) => {
    userPopup.style.display = "none";
    document.body.style.overflow = 'auto';
  })

  document.addEventListener('click', function (e) {
    let isClickIcon = user.contains(e.target)
    let isClickPopup = userPopup.contains(e.target);
    if (!isClickIcon && !isClickPopup) {
      userPopup.style.display = "none";
      document.body.style.overflow = 'auto';
    }
  })

}

function hamburger() {
  const hamburgerIcon = document.getElementById('hamburger-icon')
  const navbarNavigator = document.querySelector('.navbar-navigator');
  let is_clicked = false;
  hamburgerIcon.addEventListener('click', (e) => {

    if (!is_clicked) {
      hamburgerIcon.children[0].classList.add('fa-xmark')
      hamburgerIcon.children[0].classList.remove('fa-bars')
      navbarNavigator.style.visibility = 'visible'
      document.body.style.overflow = 'hidden'
    }
    else {
      hamburgerIcon.children[0].classList.add('fa-bars')
      hamburgerIcon.children[0].classList.remove('fa-xmark')
      navbarNavigator.style.visibility = 'hidden'
      document.body.style.overflow = 'auto'
    }
    is_clicked = !is_clicked;
  })
}

hamburger();

userProfileDetails();