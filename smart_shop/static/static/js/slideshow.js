$(document).ready(function(){
    var slideIndex =1

    const nextSlides = (slideIndex) => {
        showSlides(slideIndex += slideIndex);
    }
    const showSlides = () => {
        var i;
        var $slides = $('.index-slide');
        for (i=0; i<$slides.length; i++){
            $slides[i].style.display = "none";
        };
        slideIndex++;
        if (slideIndex > $slides.length) {slideIndex =1}
        if (slideIndex < 1) { slideIndex = $slides.length}
        $slides[slideIndex-1].style.display = "block";
        setTimeout(showSlides, 10000);
    }

    showSlides();


    $('.prev-button').click(function(){
        nextSlides(-1)
    });
    $('.next-button').click(function(){
        nextSlides(1)
    });

})




























