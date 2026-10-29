# Правила работы в команде

## Git-стратегия

Используем **GitHub Flow**: одна постоянная ветка `main`, отдельные ветки задач, слияние только через Pull Request после ревью. ADR с обоснованием: `docs/adr/001-branching-strategy.md` в одноимённой ветке до принятия и слияния.

```text
main                    A--------------B--------------C
                         \            / \            /
feature/version-endpoint  o----o------/   \          /
docs/contributing-rules                   o----o----/
```

Каждый PR решает одну задачу. Крупные изменения делим на законченные части; ориентир для обычной ветки — несколько дней. Перед созданием задачи обновляем `main`; перед слиянием получаем актуальную базу и повторяем проверки после разрешения конфликтов. История общей опубликованной ветки не переписывается.

Предлагаемый способ слияния — **Squash and merge** с итоговым сообщением Conventional Commits. После merge удаляем ненужную рабочую ветку. **Automatically delete head branches** включено владельцем 2026-10-29.

### Ветвление

Имя: `<тип>/<краткая-цель-в-kebab-case>`. Используем строчные латинские буквы, цифры и дефисы; без пробелов. Типы: `feature`, `bugfix`, `hotfix`, `docs`, `chore`.

Примеры:

- `feature/version-endpoint` — добавить `GET /version`.
- `bugfix/payment-date` — исправить расчёт даты платежа.
- `docs/adr-001-branching-strategy` — ADR о ветвлении.
- `chore/dependency-files` — файлы менеджера зависимостей.

Порядок начала работы:

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/version-endpoint
```

Документация, функции и срочные исправления проходят одинаковый цикл PR в `main`. Прямые push в `main` не используются.

### Коммиты

Используем [Conventional Commits](https://www.conventionalcommits.org/ru/v1.0.0/): `<тип>: <смысл изменения>`.

- `feat:` — новая функция.
- `fix:` — исправление ошибки.
- `docs:` — документация.
- `style:` — форматирование.
- `refactor:` — рефакторинг.
- `test:` — тесты.
- `chore:` — инфраструктура и служебные изменения.

Примеры из истории Planly:

- `feat: add initial FastAPI application with health check` — коммит `53c5228`.
- `docs: add draft ADR 001 on branching strategy` — коммит `a72d90f` в ветке ADR.

Один коммит содержит одно осмысленное изменение. Секреты, `.env`, виртуальное окружение, локальные базы и логи не коммитятся. Коммиты без описания вроде `fix` или `wip` не подходят.

## Code Review

### Регламент code review

- Автор назначает другого участника с правом записи при создании PR. Автор не одобряет собственный PR.
- Первый ответ ревьюера — в течение **24 часов** после создания PR или повторного запроса ревью.
- Автор отвечает на каждый комментарий в течение **24 часов**: правкой либо аргументом, почему правка не нужна. Если срок не выдерживается, сообщает об этом в PR и согласует новый.
- Комментарий сокомандника закрывает **тот, кто его оставил**, после проверки ответа или правки.
- Обсуждение внешнего ревьюера без права записи закрывает автор PR только после его ответа «исправлено, принимаю» в том же обсуждении или его Approve.
- После новых коммитов автор запрашивает ревью повторно: **Re-request review**. Одобрение должно относиться к последней версии.
- После двух кругов Request changes без сближения позиций вопрос обсуждается на встрече команды. Разногласие с внешним ревьюером фиксируется в рисках ADR; противоречие DoD решает преподаватель.
- На практике №2 первый круг ревью ADR завершается Request changes с минимум тремя содержательными замечаниями к строкам, затем следуют правки и повторное ревью. Сам факт этого цикла подтверждается историей PR.
- Проверка другой командой выполняется, когда преподаватель назначит её. Внутреннее ревью не записывается в отчёт как межкомандное.

### Критерии approval

Ревьюер ставит **Approve**, только если выполнены все условия:

1. В описании заполнены разделы шаблона PR и чек-лист автора. Неприменимость пункта объяснена рядом с ним.
2. Базовая ветка — `main`, имя рабочей ветки соответствует разделу «Ветвление».
3. Все новые рабочие коммиты имеют тип Conventional Commits; при squash итоговое сообщение тоже ему соответствует.
4. В diff отсутствуют секреты, `.env`, окружения и локальные базы данных.
5. Проверка из «Как проверить» воспроизведена. Для кода: приложение запускается, `GET /` и `GET /health` сохраняют ожидаемые ответы. Для документации: проверены изменённые разделы и ссылки.
6. При изменении версии/API `GET /version` возвращает `app.version` и имя `Planly`, версия согласована с `/openapi.json` и `/docs`; README описывает поведение.
7. Все замечания отвечены, обсуждения закрыты по регламенту; нет неразрешённого Request changes.
8. Для слияния есть минимум одно актуальное approval **другого участника с правом записи**. Автор проверяет это на странице PR перед merge.

Пункт 8 — условие merge: первый ревьюер не обязан ждать чужого approval, чтобы поставить своё. Если любой из пунктов 1–7 не выполнен, ревьюер выбирает **Request changes**, указывает номер критерия, конкретную строку и необходимую правку. Зелёный CI до его внедрения не является критерием approval.

### Разрешение конфликтов в коде

Если GitHub сообщает о конфликте с базой:

```bash
git switch feature/version-endpoint
git fetch origin
git merge origin/main -m "chore: sync branch with main"
```

Вместо `feature/version-endpoint` укажите свою ветку. В конфликтующих файлах выберите согласованное содержимое и удалите маркеры `<<<<<<<`, `=======`, `>>>>>>>`. Повторите проверки, затем добавьте только разрешённые файлы и завершите merge:

```bash
git add main.py README.md
git commit -m "chore: resolve merge conflict with main"
git push
```

Список файлов замените на фактически изменённые. После push нажмите **Re-request review**: при включённом сбросе устаревших approvals прежнее одобрение теряет силу. `git push --force` для разрешения конфликтов не применяется.

## Защита ветки

**Подтверждено 2026-10-29:** владелец **Владислав Журавлев (@benedIbiskit)** настроил активную защиту `main`. Состав правил проверен по публичному API; пустой bypass и автоматическое удаление рабочих веток подтверждены скриншотами владельца. Прямой push и переписывание истории отклонены GitHub, в том числе при выполнении владельцем.

Действующий [ruleset `protect-main`](https://github.com/benedIbiskit/Planly/rules/26107432):

| Настройка | Значение |
| --- | --- |
| Enforcement status | Active |
| Target branches | Include default branch — main |
| Bypass list | Пусто, включая владельца |
| Require a pull request before merging | Включено |
| Required approvals | 1 |
| Dismiss stale approvals when new commits are pushed | Включено |
| Require conversation resolution before merging | Включено |
| Restrict deletions | Включено |
| Block force pushes | Включено |
| Require status checks to pass | Выключено до практики №5 |
| Require linear history | Не требуется для выбранного GitHub Flow |

`Restrict deletions` включено; на default-ветке запрет удаления экспериментом не проверяется. Отдельной `develop` в выбранной стратегии нет. В Settings → General → Pull Requests включено **Automatically delete head branches** (подтверждено скриншотом владельца 2026-10-29).

Проверка читателем: [страница правил](https://github.com/benedIbiskit/Planly/rules/26107432) и [API ruleset](https://api.github.com/repos/benedIbiskit/Planly/rulesets/26107432). Административные изменения выполняет единственный владелец; дату, исполнителя и причину изменения правил фиксируем в этом разделе.

**Доказательства проверки**

Исполнитель — Владислав Журавлев; дата — 2026-10-29. Ниже переписаны команды и фактические сообщения об отказах со скриншотов, переданных владельцем. Подготовка и передача объектов опущены; все строки отказа сервера сохранены.

Прямой push: создан пустой пробный коммит `23fd412`; GitHub потребовал Pull Request и отклонил отправку:

```text
git commit --allow-empty -m "chore: verify branch protection"
[main 23fd412] chore: verify branch protection
git push origin main
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: Review all repository rules at https://github.com/benedIbiskit/Planly/rules?ref=refs%2Fheads%2Fmain
remote:
remote: - Changes must be made through a pull request.
remote:
To https://github.com/benedIbiskit/Planly.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/benedIbiskit/Planly.git'
```

Force-push: после возврата к `origin/main` последний серверный коммит переписан локально через `--amend` (пробный SHA `1cc0a60`). GitHub отдельно отклонил переписывание истории:

```text
git reset --hard origin/main
git commit --amend --no-edit --allow-empty
git push --force origin main
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: Review all repository rules at https://github.com/benedIbiskit/Planly/rules?ref=refs%2Fheads%2Fmain
remote:
remote: - Cannot force-push to this branch
remote:
remote: - Changes must be made through a pull request.
remote:
To https://github.com/benedIbiskit/Planly.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/benedIbiskit/Planly.git'
```

После эксперимента владелец выполнил `git fetch origin` и `git reset --hard origin/main`. Скриншот подтверждает чистое дерево и совпадение `main`, `origin/main`, `origin/HEAD` на `dd39f8a`. Пробные коммиты на сервер не попали. Эти команды описывают уже проведённый эксперимент; для обычной разработки переписывание общей истории не используется.

Первая попытка `push --force` с новым пустым коммитом проверяла только требование PR; доказательством запрета force-push служит повторный эксперимент с `--amend` и строкой `Cannot force-push to this branch` выше.

Любое временное отключение защиты фиксируется здесь: **кто, когда и зачем**. Если пробный пустой коммит всё же попал в `main`, фиксируются его SHA и дата; история сервера для его удаления не переписывается.

> TODO (модуль 3, практика №5): после появления CI-пайплайна включить в ruleset `protect-main`
> правило «Require status checks to pass» и добавить в обязательные проверки джобы
> линтера и тестов. До этого зелёный пайплайн не является условием merge.

## Как запустить тесты

TODO (модуль 3): тестов пока нет, раздел появится вместе с ними.

Сейчас выполняется ручная проверка приложения:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

В другом окне откройте `http://127.0.0.1:8000/`, `/health`, `/docs` и `/openapi.json`. Для ветки с новым эндпоинтом дополнительно проверьте `/version`: ожидается `{"version":"0.2.0","team":"Planly"}`. Для PR только с документацией запуск не требуется: неприменимость отмечается в PR. Полная инструкция окружения находится в README.

## Встречи команды

Рабочий порядок: два обсуждения в неделю в [Issues Planly](https://github.com/benedIbiskit/Planly/issues); точное время согласуем там же с участниками. Решения и итоги ревью сохраняем в Issue или PR. На обращение отвечаем в течение **24 часов**.

Изменения правил защиты планируем на обсуждение с Владиславом, поскольку только владелец может менять настройки личного репозитория.

## Разрешение конфликтов

Организационные и архитектурные споры решаем так:

1. В Issue или PR записываем вопрос, варианты и аргументы.
2. Обсуждаем всей командой; при необходимости голосуем. Для команды из трёх человек большинство — два голоса.
3. Если решение не найдено или расходится с DoD, обращаемся к преподавателю `andrey-limasov`; итог фиксируем в том же обсуждении.

Конфликты Git разрешаются по разделу «Разрешение конфликтов в коде».

## Контакты

| Участник | Роль | Способ связи |
| --- | --- | --- |
| Егор (EgorMokretsov) | Backend, подготовка ADR | [GitHub @EgorMokretsov](https://github.com/EgorMokretsov), упоминание в Issue или PR |
| Владислав Журавлев (benedIbiskit) | Владелец репозитория, настройки и координация | [GitHub @benedIbiskit](https://github.com/benedIbiskit), упоминание в Issue или PR |
| Артем Потапов | Участник разработки и ревью | Общие Issues команды с обращением по имени; GitHub-логин будет добавлен после его получения |
| Преподаватель andrey-limasov | Вопросы по требованиям курса | [GitHub @andrey-limasov](https://github.com/andrey-limasov) |

Общий канал — [Issues Planly](https://github.com/benedIbiskit/Planly/issues) и обсуждения PR; время ответа — **24 часа**. До появления логина Артема адресные вопросы ему передаёт Егор; приглашение в репозиторий отправляет Владислав после получения логина.
