// Ждем, пока вся HTML-структура страницы загрузится
document.addEventListener('DOMContentLoaded', function () {
    
    // НАШ ПЕРВЫЙ ШПИОН: Проверяем, что скрипт вообще запустился
    console.log("скрипт запущен");

    // --- ЛОГИКА ДЛЯ КАСТОМНОГО ПОЛЯ ВЫБОРА ФАЙЛА ---

    // Ищем на странице инпут для загрузки файла по его ID
    const fileInput = document.querySelector('#id_image');
    
    // ВТОРОЙ ШПИОН: Проверяем, нашел ли он наш скрытый input
    console.log("Найденный инпут:", fileInput);

    // Если такой инпут на странице найден
    if (fileInput) {
        // Находим элемент для отображения имени файла
        const filenameDisplay = document.querySelector('.file-upload-filename');
        
        // ТРЕТИЙ ШПИОН: Проверяем, нашел ли он место для текста
        console.log("Найденный дисплей:", filenameDisplay);

        // Когда пользователь выбирает файл, срабатывает событие 'change'
        fileInput.addEventListener('change', function () {
            // ЧЕТВЕРТЫЙ ШПИОН: Проверяем, сработал ли клик
            console.log("Файл изменен!", this.files[0].name);

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

});