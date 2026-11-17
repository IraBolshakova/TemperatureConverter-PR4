# Практическая работа №4 — TemperatureConverter

Проект адаптирован под Python и pytest на основе практической работы №1.

## Локальная проверка

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
$env:AI_VERSION = "ai-version-3"
py -m pytest -v --junitxml=test-results.xml
```

Для локальной проверки другой реализации задайте `$env:AI_VERSION` равным `ai-version-1` или `ai-version-2` после переключения на соответствующую ветку.

## Версии

- `ai-version-1` — Алиса
- `ai-version-2` — DeepSeek
- `ai-version-3` — GigaChat

Ветка `main` содержит базовую структуру и реализацию GigaChat (AI-v3).
## Автоматическая проверка CI

При отправке изменений в репозиторий GitHub Actions автоматически запускает тесты pytest.
