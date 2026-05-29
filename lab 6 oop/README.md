# Лабораторна робота №6
## Віртуальні середовища та сторонні бібліотеки Python

| | |
|---|---|
| **Студент** | Бейгул |
| **Дата** | 26.05.2026 |
| **Середовище** | pipenv + Python 3.13 |
| **IDE** | Visual Studio Code |

---

## 1. Перевірка pip та встановлені бібліотеки

```bash
pip -V
pip --help
pip list
```

Команда `pip --help` виводить список доступних дій: `install`, `uninstall`, `list`, `show`, `freeze` тощо.

---

## 2. Встановлення бібліотеки requests

```bash
pip install requests
```

```python
import requests
requests.__version__
r = requests.get('https://google.com')
r.status_code  # 200
```

Перевірка версії та видалення:

```bash
pip show requests
pip install requests==2.1
pip show requests
pip uninstall requests
```

---

## 3. Встановлення pipenv та створення середовища

```bash
pip install pipenv
pipenv --python 3.13
pipenv install jikanpy-v4 Flask
```

Після встановлення створились файли:
- `Pipfile` — містить список залежностей та версію Python
- `Pipfile.lock` — містить точні версії всіх бібліотек для відтворюваності середовища

---

## 4. Flask-застосунок з jikanpy

**app.py:**

```python
from flask import Flask
from jikanpy import Jikan

app = Flask(__name__)
jikan = Jikan()

j = jikan.anime(54595, extension='episodes')


@app.route('/')
def home():
    a = ""
    for episode in j["data"]:
        score = episode['score'] if episode['score'] else "Немає оцінки"
        a += f"<p>Епізод {episode['mal_id']} — <b>{episode['title']}</b>: {score}</p>"
    return a


@app.route('/season')
def current_season():
    season_data = jikan.seasons(extension='now')
    a = "<h2>Аніме поточного сезону:</h2>"
    for anime in season_data['data'][:10]:
        title = anime['title']
        score = anime['score'] if anime['score'] else "Немає оцінки"
        a += f"<p>{title} — Оцінка: {score}</p>"
    return a


if __name__ == '__main__':
    app.run(debug=True)
```

**Запуск:**

```bash
pipenv run python app.py
```

**Результат у терміналі:**

```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
127.0.0.1 - - [26/May/2026 11:46:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2026 11:46:33] "GET /season HTTP/1.1" 200 -
```

- `http://127.0.0.1:5000/` — епізоди аніме Sousou no Frieren з оцінками
- `http://127.0.0.1:5000/season` — топ-10 аніме поточного сезону

---

## 5. Файл .gitignore

```
.venv/
my_env/
__pycache__/
*.pyc
.env
```

Папки `.venv/` та `my_env/` ігноруються, оскільки містять інтерпретатор та бібліотеки середовища які не потрібно комітити.

---

## 6. Висновок

- Перевірено роботу pip та встановлено бібліотеки requests, jikanpy-v4, Flask
- Встановлено та налаштовано pipenv для управління віртуальним середовищем
- Створено Flask-застосунок з двома маршрутами
- Успішно запущено програму через `pipenv run python app.py`
- Налаштовано `.gitignore` для виключення файлів середовища
