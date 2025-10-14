// Ждем, пока вся HTML-структура страницы загрузится
document.addEventListener('DOMContentLoaded', function () {

    // --- ЛОГИКА ДЛЯ КАСТОМНОГО ПОЛЯ ВЫБОРА ФАЙЛА ---

    // Ищем на странице инпут для загрузки файла по его ID
    const fileInput = document.querySelector('#id_image');

    // Если такой инпут на странице найден
    if (fileInput) {
        // Находим элемент для отображения имени файла
        const filenameDisplay = document.querySelector('.file-upload-filename');

        // Когда пользователь выбирает файл, срабатывает событие 'change'
        fileInput.addEventListener('change', function () {
            // Если файл действительно был выбран
            if (this.files && this.files.length > 0) {
                // Показываем его имя
                filenameDisplay.textContent = this.files[0].name;
            } else {
                // Иначе показываем текст по умолчанию
                filenameDisplay.textContent = 'Файл не выбран';
            }
        });
    }

    // ВСЁ! БОЛЬШЕ НИКАКОГО КОДА ДЛЯ ФИЛЬТРАЦИИ ЗДЕСЬ БЫТЬ НЕ ДОЛЖНО.

});