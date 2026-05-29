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