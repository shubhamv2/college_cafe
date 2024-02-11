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

  initializeSwiper('.swiper1', 6000, 3, 3);
  initializeSwiper('.swiper3', 3000, 1, 3);
});