// Ждем, пока вся HTML-структура страницы загрузится
document.addEventListener('DOMContentLoaded', function () {

    // Находим все кнопки-фильтры
    const filterButtons = document.querySelectorAll('.filter-btn');

    // Находим все карточки вещей
    const itemCards = document.querySelectorAll('.item-card');

    // Проверяем, существуют ли кнопки фильтров на странице
    if (filterButtons.length > 0) {

        // Добавляем "слушатель" клика на каждую кнопку
        filterButtons.forEach(function (button) {
            button.addEventListener('click', function () {

                // Получаем значение фильтра из data-атрибута нажатой кнопки
                const filterValue = this.getAttribute('data-filter');

                // Убираем класс 'active' у всех кнопок и добавляем его только к нажатой
                filterButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');

                // Проходимся по каждой карточке
                itemCards.forEach(function (card) {
                    const cardSeason = card.getAttribute('data-season');

                    // Проверяем, нужно ли показать или спрятать карточку
                    if (filterValue === 'all' || filterValue === cardSeason) {
                        card.style.display = 'block'; // Показываем
                    } else {
                        card.style.display = 'none'; // Прячем
                    }
                });
            });
        });
    }
});