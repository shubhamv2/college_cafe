document.addEventListener('DOMContentLoaded', function () {
    function intitializeSwiper(selector, interval, slidegroup, slideview){
  
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
  
        breakpoints:{
  
          1200:{
            slidesPerView:3,
            spaceBetween:20,
          },
          718:{
            slidesPerView:2,
            spaceBetween:20,
          },
          412:{
            slidesPerView:1,
            spaceBetween:10,
          }
        }
      });
      
      setInterval(function () {
        swiper.slideNext();
      }, interval);
    }
  
  
    intitializeSwiper('.swiper1',6000,3,3)
    intitializeSwiper('.swiper2',7000,3,3)
    intitializeSwiper('.swiper3',3000,1,3)
  
  
  }
  
);
