# PoopOk

PoopOk - это веб-приложение на Django, которое позволяет пользователям отслеживать свое посещение туалета, читать и постить новости, играть в онлайн-игры и взаимодействовать с другими пользователями.

## Функциональность

### Авторизированные пользователи могут:
1. Постить/читать новости, оставлять под ними комментарии.
2. Играть онлайн в шашки/шахматы/нарды и подключать другие платформы.
3. Использовать специальные действия:
    - Кидать какахи в оппонента - 1 звезда.
    - Смывать оппонента в унитаз - 3 звезды.
    - Высрать оппонента в виде какахи и смыть - 5 звезд.
4. Обороняться от нападений или снять с себя проклятие какашечного йети, получив броню.
5. Оценивать здоровье ЖКТ по опросам и динамическим оценкам.
6. Контактировать с другими мед. сервисами и записываться на прием при недоброжелательных результатах анализа.

### Гости могут:
1. Читать новости/посты пользователей.
2. Смотреть контакты других мед. сервисов и переходить в них.

## Установка

Для установки и настройки проекта выполните следующие шаги:

1. **Клонируйте репозиторий**:
    ```sh
    git clone https://github.com/Sapientus/PoopOk
    cd poopok
    ```

2. **Создайте и активируйте виртуальное окружение**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. **Установите зависимости**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Примените миграции**:
    ```sh
    python manage.py migrate
    ```

5. **Создайте суперпользователя**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Запустите сервер разработки**:
    ```sh
    python manage.py runserver
    ```

## Развертывание

Для развертывания проекта на продакшн-сервере, выполните следующие шаги:

### Использование Gunicorn

1. **Установите Gunicorn**:
    ```sh
    pip install gunicorn
    ```

2. **Запустите Gunicorn**:
    ```sh
    gunicorn poopok.wsgi:application
    ```

### Использование uWSGI

1. **Установите uWSGI**:
    ```sh
    pip install uwsgi
    ```

2. **Создайте файл конфигурации `uwsgi.ini`**:
    ```ini
    [uwsgi]
    module = poopok.wsgi:application
    master = true
    processes = 4
    socket = 127.0.0.1:8000
    vacuum = true
    die-on-term = true
    ```

3. **Запустите uWSGI**:
    ```sh
    uwsgi --ini uwsgi.ini
    ```

### Использование Apache с mod_wsgi

1. **Установите и настройте mod_wsgi**:
    Добавьте следующую конфигурацию в ваш файл Apache (например, `httpd.conf` или файл виртуального хоста):
    ```apache
    WSGIDaemonProcess poopok python-path=/path/to/your/project
    WSGIProcessGroup poopok
    WSGIScriptAlias / /path/to/your/project/poopok/wsgi.py

    <Directory /path/to/your/project/poopok>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    ```

2. **Перезапустите Apache**:
    ```sh
    sudo systemctl restart apache2
    ```

# Структура проекта

```plaintext
poopok/
    manage.py
    poopok/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    core/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    news/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        forms.py
        urls.py
        templates/
            news/
                post_list.html
                post_detail.html
                create_post.html
    games/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        forms.py
        urls.py
        templates/
            games/
                create_game_session.html
                game_session_list.html
    stars/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        forms.py
        urls.py
        templates/
            stars/
                star_balance.html
                perform_action.html
    health/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        forms.py
        urls.py
        templates/
            health/
                health_survey.html
                health_survey_results.html
                medical_services.html
```

## Пояснение структуры

- `poopok/` — Корневая директория проекта.
  - `manage.py` — Скрипт для выполнения административных команд.
  - `poopok/` — Каталог конфигурации проекта.
    - `__init__.py` — Инициализирующий файл пакета.
    - `settings.py` — Настройки проекта.
    - `urls.py` — URL-конфигурация проекта.
    - `wsgi.py` — WSGI-конфигурация для развертывания проекта.
  - `core/` — Основное приложение проекта.
    - `__init__.py` — Инициализирующий файл пакета.
    - `admin.py` — Регистрация моделей в административном интерфейсе.
    - `apps.py` — Конфигурация приложения.
    - `models.py` — Определение моделей.
    - `tests.py` — Тесты приложения.
    - `views.py` — Представления.
  - `news/` — Приложение для новостей.
    - `__init__.py` — Инициализирующий файл пакета.
    - `admin.py` — Регистрация моделей в административном интерфейсе.
    - `apps.py` — Конфигурация приложения.
    - `models.py` — Определение моделей.
    - `tests.py` — Тесты приложения.
    - `views.py` — Представления.
    - `forms.py` — Формы для приложения.
    - `urls.py` — URL-конфигурация приложения.
    - `templates/` — Шаблоны для приложения.
      - `news/` — Шаблоны для модуля новостей.
        - `post_list.html` — Шаблон списка постов.
        - `post_detail.html` — Шаблон детали поста.
        - `create_post.html` — Шаблон создания поста.
  - `games/` — Приложение для игр.
    - `__init__.py` — Инициализирующий файл пакета.
    - `admin.py` — Регистрация моделей в административном интерфейсе.
    - `apps.py` — Конфигурация приложения.
    - `models.py` — Определение моделей.
    - `tests.py` — Тесты приложения.
    - `views.py` — Представления.
    - `forms.py` — Формы для приложения.
    - `urls.py` — URL-конфигурация приложения.
    - `templates/` — Шаблоны для приложения.
      - `games/` — Шаблоны для модуля игр.
        - `create_game_session.html` — Шаблон создания игровой сессии.
        - `game_session_list.html` — Шаблон списка игровых сессий.
  - `stars/` — Приложение для управления звездами.
    - `__init__.py` — Инициализирующий файл пакета.
    - `admin.py` — Регистрация моделей в административном интерфейсе.
    - `apps.py` — Конфигурация приложения.
    - `models.py` — Определение моделей.
    - `tests.py` — Тесты приложения.
    - `views.py` — Представления.
    - `forms.py` — Формы для приложения.
    - `urls.py` — URL-конфигурация приложения.
    - `templates/` — Шаблоны для приложения.
      - `stars/` — Шаблоны для модуля звезд.
        - `star_balance.html` — Шаблон баланса звезд.
        - `perform_action.html` — Шаблон выполнения действий.
  - `health/` — Приложение для оценки здоровья ЖКТ.
    - `__init__.py` — Инициализирующий файл пакета.
    - `admin.py` — Регистрация моделей в административном интерфейсе.
    - `apps.py` — Конфигурация приложения.
    - `models.py` — Определение моделей.
    - `tests.py` — Тесты приложения.
    - `views.py` — Представления.
    - `forms.py` — Формы для приложения.
    - `urls.py` — URL-конфигурация приложения.
    - `templates/` — Шаблоны для приложения.
      - `health/` — Шаблоны для модуля здоровья.
        - `health_survey.html` — Шаблон опроса здоровья.
        - `health_survey_results.html` — Шаблон результатов опроса здоровья.
        - `medical_services.html` — Шаблон для мед. сервисов.

