# AI Агенти з Google ADK

Лабораторна робота з AI агентів на основі Google ADK.

## Структура проекту

```
06_python_agents/
├── my_first_agent/       # Агент часу
├── math_agent/           # Математичний агент
├── student_helper/       # Помічник студента
├── creative_writer/      # Креативний письменник
├── conversation_agent/   # Розмовний агент з пам'яттю
├── stateful_agent/       # Агент зі збереженням між сесіями
├── code_pipeline/        # Sequential агент
├── story_improver/       # Loop агент
├── research_team/        # Parallel агент
├── tools/                # Спільні інструменти
├── pyproject.toml
└── poetry.lock
```

## Запуск

```bash
# Встановлення залежностей
poetry install

# Запуск агента через термінал
poetry run adk run my_first_agent

# Запуск веб-інтерфейсу
poetry run adk web --port 8000
```

## Налаштування

У кожній папці агента створіть файл `.env`:
```
GOOGLE_API_KEY="ваш_ключ_тут"
```
