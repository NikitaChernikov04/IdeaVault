// cards.js

document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');
    const dislikeButtons = document.querySelectorAll('.dislike-button');

    likeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Добавить логику для обработки лайка
            console.log('Liked');
        });
    });

    dislikeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Добавить логику для обработки дизлайка
            console.log('Disliked');
        });
    });
});