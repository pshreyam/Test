import requests
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    r = requests.get(url).json()
    return r

@app.route('/',methods = ['GET','POST'])
def index(): 
    if request.method == "POST":
        err_msg = ''
        new_city = request.form['city'].title()
        if new_city:
            existing_city = City.query.filter_by(name = new_city).first()
            if not existing_city:
                new_city_data = get_weather_data(new_city)
                if new_city_data['cod'] == 200:
                    new_city_obj = City(name = new_city)
                    db.session.add(new_city_obj)
                    db.session.commit()
                else:
                    err_msg = 'City does not exist in the world!'
            else:
                err_msg = 'City already exists in the database!'
        if err_msg:
            flash(err_msg, 'error')
        else:
            flash('City added successfully!', 'success')
        return redirect(url_for('index'))

    cities = City.query.all()
    weather_data = []
    for city in cities:
        r = get_weather_data(city.name)
        weather = {
            'id': city.id,
            'city': city.name,
            'temperature_f': round(r['main']['temp'], 2),
            'temperature_c': round((r['main']['temp'] - 32) * (5 / 9), 2),
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(weather)
        weather_data.reverse()
    return render_template('weather.html', weather_data=weather_data)

@app.route('/delete/<int:id>')
def delete(id):
    city = City.query.filter_by(id=id).first()
    db.session.delete(city)
    db.session.commit()
    flash(f"Successfully deleted: { city.name }!", 'success') 
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
