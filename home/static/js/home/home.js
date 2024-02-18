document.addEventListener('DOMContentLoaded', function () {
  function initializeSwiper(selector, interval, slidegroup, slideview) {
      const swiper = new Swiper(selector, {
          slidesPerView: slideview,
          spaceBetween: 30,
          slidesPerGroup: slidegroup,
          loopFillGroupWithBlank: true,
          loop: true,
          pagination: {
              el: `${selector} .swiper-pagination`,
              clickable: true,
          },
          navigation: {
              nextEl: `${selector} .swiper-button-next`,
              prevEl: `${selector} .swiper-button-prev`,
          },
          breakpoints: {
              300: {
                  slidesPerView: 1,
                  spaceBetween: 10,
              },
              718: {
                  slidesPerView: 2,
                  spaceBetween: 20,
              },
              1200: {
                  slidesPerView: 3,
                  spaceBetween: 20,
              },
          }
      });

      setInterval(function () {
          swiper.slideNext();
      }, interval);
  }

  function validateForm(){
    const reviewField = document.getElementById('review-field');
    const messageDiv = document.getElementById('message-div')
    const sendBtn = document.querySelector('.send-btn')
    const message = document.getElementById('message')
    sendBtn.addEventListener('click',(e)=>{
        if(reviewField.value.trim() === ''){
            e.preventDefault()
            reviewField.style.border = '1px solid red';
            message.textContent = 'Review field is empty!';
            message.style.color = 'red';
        }

    })
  }
  validateForm()
  initializeSwiper('.swiper1', 6000, 3, 3);
  initializeSwiper('.swiper3', 3000, 1, 3);
});