from flask import Flask, render_template
import requests
import random
from config import api_key

app = Flask(__name__)

# Списки городов Америки, Британии и Европы
usa_cities = ['Atlanta', 'Yuma', 'San Francisco', 'Boston', 'Washington', 'New York', 'Las Vegas', 'Forks', 'Chicago', 'Philadelphia', 'Nashville']
europe_cities = ['Prague', 'Brno', 'Karlovy Vary', 'Liberec', 'Stockholm', 'Gothenburg', 'Malmo']
british_cities = ['London', 'Bristol', 'Coventry', 'Bath', 'Glasgow', 'Edinburgh', 'Manchester']

@app.route('/', methods=['GET'])
def index():
    # Выбираем случайный город из Америки, Европы или Британии
    city = random.choice(usa_cities + europe_cities + british_cities)

    # Получаем погоду для выбранного города
    weather = get_weather(city)

    # Передаем данные о погоде в шаблон
    return render_template("index.html", weather=weather, city=city)

# Функция для получения погоды
def get_weather(city):
    # Формируем запрос с параметром lang=ru для вывода на русском
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)

    # Возвращаем результат запроса в формате JSON
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
