# Yacut

> Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Технологии проекта

- Python — высокоуровневый язык программирования.
- Flask — фреймворк для создания веб-приложений.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/BuriloT/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

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

Создайте и заполните файл .env:

```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```

Выполните миграции:

```
flask db upgrade
```

Запустите проект:

```
flask run
```

### Примеры запросов:

GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору:

```
/api/id/{short_id}/
```

Request:

```
{
  "url": "string"
}
```

POST-запрос на создание новой короткой ссылки:

```
/api/id/
```

Request:

```
{
  "url": "string",
  "custom_id": "string"
}
```
