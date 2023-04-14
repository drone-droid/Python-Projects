from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        location = request.form['location']
        api_key = 'fce1c8ed838180cacc6f2bf5079a3b4d'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = json.loads(response.text)
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return render_template('weather.html', weather=weather)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
