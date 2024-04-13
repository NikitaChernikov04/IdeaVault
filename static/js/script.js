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

// Получаем ссылки на элементы страницы
const createIdeaBtn = document.getElementById('create-idea-btn');
const newIdeaForm = document.getElementById('new-idea-form');
const saveBtn = document.querySelector('#new-idea-form .save-btn');

// Добавляем обработчик события для кнопки "Создать свою идею"
createIdeaBtn.addEventListener('click', function() {
    newIdeaForm.style.display = 'block'; // Показываем пустую карточку
});

// Добавляем обработчик события для кнопки "Сохранить"
saveBtn.addEventListener('click', function() {
    const textarea = document.querySelector('#new-idea-form textarea');
    const ideaText = textarea.value.trim();
    
    if (ideaText !== '') {
        const newCard = document.createElement('div');
        newCard.classList.add('card');
        newCard.innerHTML = `
            <h2>Новая идея</h2>
            <p class="idea">${ideaText}</p>
            <button class="read-more-btn">Читать полностью</button>
            <button class="like-btn">👍</button>
            <button class="delete-btn">Удалить запись</button>
        `;
        document.querySelector('.card-container').appendChild(newCard);
        newIdeaForm.style.display = 'none'; // Скрываем форму
        textarea.value = ''; // Очищаем текстовое поле
    } else {
        alert('Введите вашу идею!');
    }
});

// Добавляем обработчик события для кнопок "Читать полностью"
document.querySelectorAll('.read-more-btn').forEach(button => {
    button.addEventListener('click', function() {
        const card = this.closest('.card');
        const idea = card.querySelector('.idea');
        idea.style.maxHeight = 'none';
        this.style.display = 'none'; // Скрываем кнопку
    });
});

// Добавляем обработчик события для кнопок "👍"
document.querySelectorAll('.like-btn').forEach(button => {
    button.addEventListener('click', function() {
        // Добавьте ваш код для обработки нажатия на кнопку "👍"
    });
});

// Добавляем обработчик события для кнопок "Удалить запись"
document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function() {
        const card = this.closest('.card');
        card.remove(); // Удаляем карточку
    });
});