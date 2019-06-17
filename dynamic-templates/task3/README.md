Фильтры для шаблонов
=======

Приложение выводит самые лучшие свежие посты из сабреддита, посвященному Python (reddit.com/r/Python).

В директории `templatetags/news_filters.py` необходимо реализовать следующие фильтры:

- `format_date`: форматирует дату по следующим правилам

1. Если пост был меньше 10 минут назад, пишет "только что"
2. Если пост был меньше 24 часов назад, пишет "X часов назад"
3. Если пост был больше 24 часов назад, выводит дату в формате "Год-месяц-число"

- форматирование поля `score` (название на ваше усмотрение):

1. Рейтинг меньше -5, пишет "все плохо"
2. Рейтинг от -5 до 5 – "нейтрально"
3. Рейтинг больше 5 – "хорошо"

Если поле `score` отсутствует, то рендерится дефолтное значение, которое передается в качестве параметра фильтра.

- `format_num_comments`:

1. Если комментариев 0, пишется "Оставьте комментарий"
2. От 0 до 50, пишем число комментариев
3. Больше 50, пишем "50+"

- `format_selftext`:

Оставляет `count` первых и `count` последних слов, между ними должно быть троеточие. `count` задается параметром фильтра. Пример c `count = 5`: `"Hi all sorry if this ... help or advice greatly appreciated."`

Знаки препинания остаются, обрезаются только слова.


## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить команду:

```bash
python manage.py runserver
```