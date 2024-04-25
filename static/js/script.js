document.addEventListener('DOMContentLoaded', function () {
    window.addEventListener('scroll', function () {
        let animatedContent = document.getElementById('animatedContent');
        let positionFromTop = animatedContent.getBoundingClientRect().top;

        // Вычисляем, когда элемент появляется на экране при прокрутке
        let screenHeight = window.innerHeight;
        if (positionFromTop - screenHeight <= 0) {
            animatedContent.classList.add('visible');
        } else {
            animatedContent.classList.remove('visible');
        }
    });
});
