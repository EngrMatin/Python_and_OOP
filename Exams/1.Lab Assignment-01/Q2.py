import requests
import json
import time

def weather_data():

    api_key = "f7725593820578286571c4649a39ccc9"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Dhaka"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    response = requests.get(complete_url)
    x = response.json()
    
    if x['cod'] != "404":
    
        y = x["main"]
    
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]

        z = x["weather"]
    
        weather_description = z[0]["description"]
    
        print("\n Temperature (in Kelvin unit) = " + str(current_temperature) +
            "\n Atmospheric Pressure (in hPa unit) = " + str(current_pressure) +
            "\n Humidity (in percentage) = " + str(current_humidity) +
            "\n Description = " + str(weather_description))
    
    else:
        print(" City Not Found ")

while True:
    weather_data()
    time.sleep(30*60)
