# Система бронирования отелей API

## Описание
Система бронирования отелей - это веб-приложение, разработанное на Python с использованием FastAPI для управления бронированиями отелей.

## Технологии
- Python 3
- FastAPI
- SQLAlchemy
- Alembic
- Pytest
- Ruff

## Структура проекта
```
hotel_booking_system/
├── src/                    # Исходный код приложения
│   ├── database/          # Конфигурация базы данных
│   ├── models.py          # Модели данных
│   ├── schemas/           # Pydantic схемы
│   ├── repository/        # Слой доступа к данным
│   ├── routers.py         # API маршруты
│   └── main.py           # Точка входа приложения
├── tests/                 # Тесты
├── alembic/              # Миграции базы данных
└── venv/                 # Виртуальное окружение Python
```

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone [url-репозитория]
cd hotel_booking_system
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```
или
```bash
poetry install
```


4. Настройте базу данных:
```bash
alembic upgrade head
```

5. Запустите приложение:
```bash
python src/main.py
```

## API Endpoints

API будет доступно по адресу: `http://localhost:8000`

Документация API (Swagger UI): `http://localhost:8000/docs`

## Тестирование

Для запуска тестов используйте:
```bash
pytest
```

## Линтинг

Для проверки кода используйте:
```bash
./lint.sh
```
