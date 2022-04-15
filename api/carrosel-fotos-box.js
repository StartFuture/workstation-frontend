const $thumbsCarousel = document.querySelector(".js-carousel--thumbs");
const $thumbs = document.querySelectorAll("[data-carousel-index]");
const thumbsGlider = new Glider($thumbsCarousel, {
    slidesToShow: 1,
    slidesToScroll: 1,
    draggable: true,
    duration: 0.25,
    arrows: {
        prev: ".js-carousel--responsive-prev",
        next: ".js-carousel--responsive-next",
    },
    responsive: [{
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
        },
    }, ],
});

$thumbs.forEach($t => {
    $t.addEventListener("click", e => {
        const index = e.target.getAttribute("data-carousel-index");

        thumbsGlider.scrollItem(index, true);
    });
});