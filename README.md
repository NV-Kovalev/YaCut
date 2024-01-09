# Проект Yacut

## Используемые технолологии:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/Flask-005571?style=for-the-badge&logo=Flask)
![sqlalchemy](https://img.shields.io/badge/sqlalchemy-%2300f.svg?style=for-the-badge)

## Сервис позволяющий укорачивать ссылки с помощью редиректа через наш сайт. Учебный проект на Flask

## Используемые технолологии:

Flask
sqlalchemy

## Как запустить проект:

Создать .env файл внутри директории проекта

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
