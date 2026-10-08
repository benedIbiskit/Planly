# Planly

Planly — приложение для управления подписками. Проект поможет хранить сведения о сервисах, стоимости и датах следующих платежей, чтобы планировать расходы. В практике №1 подготовлены правила командной работы и минимальный backend на FastAPI.

## Команда

- [benedIbiskit](https://github.com/benedIbiskit) — владелец репозитория, координация проекта.
- [Егор (EgorMokretsov)](https://github.com/EgorMokretsov) — участник разработки backend.

Состав команды и распределение ролей уточняются участниками в Pull Request.

## Стек технологий

- Python 3.11+ (проверено на Python 3.12).
- FastAPI — HTTP API и автоматическая документация OpenAPI.
- Uvicorn — сервер приложения.
- Git и GitHub — версии кода и Code Review.
- PostgreSQL, Docker и GitHub Actions — планируются в следующих практиках.

## Статус

Проект в разработке. Практика №1: инфраструктура команды и базовое приложение. Управление подписками будет реализовано на следующих этапах.

## Установка и запуск

### Клонирование

```bash
git clone https://github.com/benedIbiskit/Planly.git
cd Planly
```

Пока Pull Request практики №1 открыт, переключитесь на ветку приложения:

```bash
git switch feature/initial-setup
```

### Виртуальное окружение

На macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

На Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Зависимости и сервер

После активации окружения:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Сервер доступен по адресу `http://127.0.0.1:8000`.

| Адрес | Результат |
| --- | --- |
| `GET /` | `{"message": "Hello World"}` |
| `GET /health` | `{"status": "healthy"}` |
| `/docs` | Интерактивная документация Swagger UI |
| `/openapi.json` | Схема OpenAPI |

Для остановки сервера нажмите `Ctrl+C`. Окружение `venv/` создаётся локально и исключено из Git.

## Участие в разработке

Правила ветвления, коммитов и ревью: [CONTRIBUTING.md](CONTRIBUTING.md).
Отчёт и чек-лист практики: [docs/practice-1.md](docs/practice-1.md) в ветке `feature/initial-setup`.

## Лицензия

[MIT](LICENSE).
