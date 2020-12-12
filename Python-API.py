import requests
import json
import os
from pprint import pprint

possibilities = {"clouds", "cod", "coord", "dt", "id", "main", "name", "sys", "timezone", "visibility", "weather"}
menu = '''
_____________________________________________________________________________
| type q to select another country.                                         |
| hier onder in het menu staat een lijst met keuzes waaruit je kan kiezen.  |
| mogelijke keuzes: clouds, cod, coord, dt, id, main, name, sys, timezone,  |
| visibility and weather.                                                   |
|___________________________________________________________________________|
'''

def API_Choice(the_API):
    api_key = "3765ece0add2b4d1a2211ebc344295e4"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter the city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    the_API = response.json()
    pprint(the_API)
    return the_API

def user_choices(the_API):
    print(menu)
    choice = input("What do you want to search press q to choice a new city : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "q":
        runner_code()
    elif choice in possibilities:
        print(the_API['choice'])
    else:
        print("That is not possible. ")

def runner_code():
    API_Choice(the_API)
    again = True
    while again:
        user_choices(the_API)

runner_code()
