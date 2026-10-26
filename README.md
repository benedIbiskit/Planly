# Planly

Planly — приложение для управления подписками. Проект поможет хранить сведения о сервисах, стоимости и датах следующих платежей, чтобы планировать расходы. В практике №1 подготовлены правила командной работы и минимальный backend на FastAPI.

## Команда

- [Егор (EgorMokretsov)](https://github.com/EgorMokretsov) — разработка backend, подготовка ADR.
- [Владислав Журавлев (benedIbiskit)](https://github.com/benedIbiskit) — владелец репозитория, координация проекта и настройки GitHub.
- Артем Потапов — участник разработки и ревью. GitHub-логин будет добавлен позже; после его получения владелец пригласит Артема в репозиторий.

Канал связи — [Issues проекта](https://github.com/benedIbiskit/Planly/issues) и обсуждения Pull Request.

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

Приложение практики №1 находится в `main`. Для разработки создавайте отдельную ветку по правилам CONTRIBUTING.md.

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
Отчёт практики №1: [docs/practice-1.md](docs/practice-1.md). Он сохраняет состояние на момент подготовки; фактическое слияние подтверждается [PR №1](https://github.com/benedIbiskit/Planly/pull/1).

## Лицензия

[MIT](LICENSE).
