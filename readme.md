# Что это за репозиторий такой?

Это сборник блокнотов на тему компьютерного зрения.

# Структура репозитория 

Одна папка - один проект. Пректы указаны снизу. Про каждый проект указана базовая информация, дабы если Вы здесь для того, чтобы посмотреть на блокноты, что относятся к задачам определённого типа, Вам их было легче найти. Базовая информация включает в себя:
1. Устройство данных (таблица, текст, аудио и т.д)
2. Тип задачи (классификация, регрессия, ранжирование и т.д)
3. Подход к решению (классические/нейросетевые методы или комбинированный подход) 
4. Основные использованные в проекте библиотеки
5. Краткое описание непосредственно данных

Более подробная информация о каждом из проектов в `readme` соответствующей папки. Если явно не оговорено обратное, используется Python. Список снизу приведён в порядке, обратном к хронологическому

# Очень важно
Все рассуждения в присутствующих тут блокнотах на правильность ни в коем случае не претендуют. Использовать эти блокноты с целью научиться несредственно машинному обучению я бы не рекомендовал. Единственное, чему отсюда можно именно научиться - это избегать грабель, что сжигают и нервы, и кучу времени.

# Facades Segmentation

1. Устройство данных: фотографии зданий с соответствующими масками
2. Тип задачи: сегментация
3. Подход к решению: нейросетевой. Конкретнее, используются полностью свёрточные сети с SegNet и UNet архитектурами
4. Основные использованные библиотеки: tensorflow, pandas, numpy, matplotlib
5. Краткое описание данных: было описано выше. Подробнее в самом начале [этого](https://github.com/ontoshenka/Notebooks/blob/master/Facades%20Segmentation/modelling.ipynb) блокнота
