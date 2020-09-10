import click
import requests,json
from datetime import datetime
from decouple import config

API_KEY = config("API_KEY")
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@click.group()
def cli():
    pass

@cli.command(name="weather")
@click.option('--celcius',default=False,is_flag=True,type=click.BOOL, help='only alphabet')
@click.option('--fahrenheit',default=False,is_flag=True,type=click.BOOL, help='only alphabet')
@click.option('--temp',default=False,is_flag=True,type=click.BOOL, help='only alphabet')
@click.argument('sentence',default=False,type=click.STRING)
def weather(sentence,celcius,fahrenheit,temp):
    city_name = sentence
    complete_url = base_url + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url).json()
    data = json.dumps(response, indent= 4)
    # print(data)
    if response["cod"] != "404":
        city = response["name"]
        a = response["main"]
        temperature = a["temp"]
        if celcius == True:
            temperature = temperature - 273.15
        if fahrenheit == True:
            temperature = (temperature- 273.15)*1.8000+32.00
        b = response["dt"]
        dateTime = datetime.utcfromtimestamp(b).strftime('%c')
        c = response["sys"]
        sunrise = c["sunrise"]
        dateSunrise = datetime.utcfromtimestamp(sunrise).strftime('%c')
        sunset = c["sunset"]
        dateSunset = datetime.utcfromtimestamp(sunset).strftime('%c')
        z = response["weather"]
        cuaca = z[0]["main"]
        weather_description = z[0]["description"]
        
        

        print(f"datetime    : {dateTime}")
        print(f"city        : {city}")
        print(f"Temperature : {temperature}")
        print(f"weather     : {cuaca}, {weather_description}")
        print(f"sunrise     : {dateSunrise}")
        print(f"sunset      : {dateSunset}")

        if temp == True:
            print(f"{city}, {dateTime}")
            print("-----------------------")
            print(f"{temperature} | {cuaca},{weather_description}")

    else: 
        print(" City Not Found ")
    
if __name__ == "__main__":
    cli()
