# Сайт-визитка на Django (начинающий уровень)

Простой проект, который показывает информацию о человеке: имя, описание, навыки и контакты.

## Быстрый запуск

1. Создайте и активируйте виртуальное окружение:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

2. Установите зависимости:

```powershell
pip install -r requirements.txt
```

3. Примените миграции:

```powershell
python manage.py migrate
```

4. Запустите сервер:

```powershell
python manage.py runserver
```

5. Откройте в браузере:

`http://127.0.0.1:8000/`

## Где менять данные

Информация о человеке находится в файле `main/views.py` в словаре `context`.
