class Carousel {
    constructor(options)
    {
        this.options = options;
        this.elements = {
            carousel_main : document.querySelector('.'),
            carousel_items: document.querySelector('.'),
            carousel_next_btn: document.querySelector('.'),
            carousel_prev_btn: document.querySelector('.'),
        }
        this.addListeners();
    }
    addListeners(){
        document.addEventListener('DOMContentLoaded', function () {
        var carousel = document.getElementById('myCarousel');
        var carouselInner = carousel.querySelector('.carousel-inner');
        var items = carouselInner.querySelectorAll('.carousel-item');
        var currentIndex = 0;
    
        function showSlide(index) {
            if (index < 0) {
            index = items.length - 1;
            } else if (index >= items.length) {
            index = 0;
            }
            var newTransformValue = -index * 100 + '%';
            carouselInner.style.transform = 'translateX(' + newTransformValue + ')';
            currentIndex = index;
        }
    
        function nextSlide() {
            showSlide(currentIndex + 1);
        }
    
        function prevSlide() {
            showSlide(currentIndex - 1);
        }
    
        // Add event listeners to navigation buttons
        document.querySelector('.carousel-next').addEventListener('click', nextSlide);
        document.querySelector('.carousel-prev').addEventListener('click', prevSlide);
    
        // Optionally, you can add automatic sliding
        //setInterval(nextSlide, 2000); // Change the interval as needed (e.g., 2000 = 2 seconds)
        });
    }
}