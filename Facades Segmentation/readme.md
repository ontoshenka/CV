# Информация об отдельных файлах и каталогах

`modelling.ipynb` - блокнот с непосредственно моделями

`paths.py` - ряд путей к файлам из датасетов. Пригождается и в блокноте, в и `pre_process.py`, поэтому вынесено в отдельный файл

`pre_process.py` - приводит изначально немного по-разному хранимые данные из разных датасетов к более удобному формату и конвертирует все фото и маски в jpg

`backgrounds` - фотографии фонов, на которые будут лепиться здания из найденных датасетов. Подробнее - в блокноте

`test_data` - несколько фотографий зданий, которые не участвовали в обучении

# Грабли

Если надумаете использовать полностью свёрточные SegNet или UNet архитектуры, помните, что если MaxPool (а равно и UpSampling) слоёв $n$, то каждое измерение входа должно делиться на $2^{n}$, ибо иначе размерность входа не будет совпадать с размерностью выхода и будет невозможно посчитать перекрёстную энтропию и другие функции потери 

