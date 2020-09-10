import click
import requests,json
from datetime import datetime
from decouple import config

API_KEY = config("API_KEY")
base_url = "http://api.openweathermap.org/data/2.5/forecast?"


@click.group()
def cli():
    pass

@cli.command(name="forecast")
@click.argument('sentence')
def forecast(sentence):
    city_name = sentence
    complete_url = base_url +"q=" +city_name +"&appid=" + API_KEY 
    response = requests.get(complete_url).json()
    data = json.dumps(response, indent= 4)

    if response["cod"] != "404":
        a   = response["city"]
        city = a["name"]

        b = response["list"]
        c = b[0]["dt"]
        dateTime = datetime.utcfromtimestamp(c).strftime('%c')

        d = response["list"]
        time = d[0]["dt_txt"]
        
        e = response["list"]
        temperature = e[0]["main"]["temp"]

        z = response["list"]
        cuaca = z[0]["weather"][0]["main"]
        weather_description = z[0]["weather"][0]["description"]
        
        print(f"{city}, {dateTime}")
        print("-----------------------------------")
        print(f"{time} | {temperature} | {cuaca},{weather_description}")

    else: 
        print(" City Not Found ")

if __name__ == "__main__":
    cli()
