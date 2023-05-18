# YaCut
Проект YaCut — это сервис укорачивания ссылок (связывает длинную ссылку с короткой ссылкой, предоставленной пользователем).

## Ключевые возможности сервиса
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам

## Доступны web и api интерфейсы.

## Технологии
- Python 3.10.7
- Flask 2.0.2
- Jinja2 3.0.3
- SQLAlchemy 1.4.29
- Alembic 1.7.5

### Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
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

Создать файл настроек окружения:
```
touch .env
```
Заполнить его:
```
FLASK_APP=yacut
FLASK_ENV=production
DATABASE_URI=<sqlite:///db.sqlite3>
SECRET_KEY=<Your secret key>
```
Запустить:
```
flask run
```
