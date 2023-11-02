### Проект Yacut

## Сервис позволяющий укорачивать ссылки с помощью редиректа через наш сайт.


## Команда разработчиков:
backend: Никита Ковалев
frontend: Yandex Practicum

## Используемые технолологии:

Flask
sqlalchemy

## Как запустить проект:


Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Создать .env файл внутри директории проекта:

Пример файла .env

```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=SECRET_KEY
HOST=http://localhost/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## База данных:

```
flask shell

from yacut.__init__ import db

db.create_all()
```

## Запуск сервера:

```
flask run
```