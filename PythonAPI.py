import requests
import json
import os
import sys
from pprint import pprint

SCREEN_WIDTH = 80
MAX_WORD_LENGTH = 40

possibilities = {"clouds", "wind", "cod", "coord", "dt", "id", "main", "name", "sys", "timezone", "visibility", "weather"}
main_possibilities = {"feels_like", "humidity", "pressure", "temp", "temp_max", "temp_min"}
sys_possibilities = {"country", "id", "sunrise", "sunset", "type"}
wind_possibilities = {"deg", "speed"}
coord_possibilities = {"lat", "lon"}

menu = '''
_____________________________________________________________________________
| type q to select another country.                                         |
| type k to show the complete API.                                          |
| This menu contains the choices you can choose from.                       |
| pissible choices: clouds, wind, cod, coord, dt, id, main, name, sys,      |
| timezone, visibility and weather.                                         |
|___________________________________________________________________________|
'''
main_menu = '''
_____________________________________________________________________________
| Choose from: feels_like, humidity, pressure, temp, temp_max, temp_min     |
|___________________________________________________________________________|
'''
sys_menu = '''
_____________________________________________________________________________
| Choose from: country, id, sunrise, sunset, type                           |
|___________________________________________________________________________|
'''
wind_menu = '''
_____________________________________________________________________________
| Choose from: deg, speed                                                   |
|___________________________________________________________________________|
'''
coord_menu = '''
_____________________________________________________________________________
| Choose from: lat, lon                                                     |
|___________________________________________________________________________|
'''

def print_regel(regel):
    print(("| {:" + str(MAX_WORD_LENGTH - 4)+ "} |").format(regel))

def main_choice_def(the_API, choice):
    print(main_menu)
    main_choice = input("Type 1 to show all info from (main) or to get a specific part type one of the things that is in the menu above : ")
    if main_choice in main_possibilities:
        print_regel(("input user: {:^" + str(MAX_WORD_LENGTH) + "} output program: {:^" + str(MAX_WORD_LENGTH) + "}").format("[" + choice + ", " + main_choice + "]", the_API[choice][main_choice]))
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pprint(the_API[choice])
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')

def sys_choice_def(the_API, choice):
    print(sys_menu)
    sys_choice = input("Type 1 to show all info from (sys) or to get a specific part type one of the things that is in the menu above : ")
    if sys_choice in sys_possibilities:
        print_regel(("input user: {:^" + str(MAX_WORD_LENGTH) + "} output program: {:^" + str(MAX_WORD_LENGTH) + "}").format("[" + choice + ", " + sys_choice + "]", the_API[choice][sys_choice]))
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pprint(the_API[choice])
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')

def wind_choice_def(the_API, choice):
    print(wind_menu)
    wind_choice = input("Type 1 to show all info from (wind) or to get a specific part type one of the things that is in the menu above : ")
    if wind_choice in wind_possibilities:
        print_regel(("input user: {:^" + str(MAX_WORD_LENGTH) + "} output program: {:^" + str(MAX_WORD_LENGTH) + "}").format("[" + choice + ", " + wind_choice + "]", the_API[choice][wind_choice]))
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pprint(the_API[choice])
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')

def coord_choice_def(the_API, choice):
    print(coord_menu)
    coord_choice = input("Type 1 to show all info from (wind) or to get a specific part type one of the things that is in the menu above : ")
    if coord_choice in coord_possibilities:
        print_regel(("input user: {:^" + str(MAX_WORD_LENGTH) + "} output program: {:^" + str(MAX_WORD_LENGTH) + "}").format("[" + choice + ", " + coord_choice + "]", the_API[choice][coord_choice]))
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pprint(the_API[choice])
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')

def cloud_choice_def(the_API, choice):
    print_regel(("input user: {:^" + str(MAX_WORD_LENGTH) + "} output program: {:^" + str(MAX_WORD_LENGTH) + "}").format("[" + choice + "]", the_API[choice]['all']))
    input_enter = input("Press enter to go back : ")
    os.system('cls' if os.name == 'nt' else 'clear')

def weather_choice_def(the_API, choice):
    pprint(the_API[choice])
    input_enter = input("Press enter to go back : ")
    os.system('cls' if os.name == 'nt' else 'clear')

def runner_code():
    os.system('cls' if os.name == 'nt' else 'clear')
    api_key = "3765ece0add2b4d1a2211ebc344295e4"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter the city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    the_API = response.json()
    if the_API["cod"] != "404":
        again = True
        while again:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(menu)
            choice = input("What is your choice out of the menu press q to choice a new city : ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "q":
                runner_code()
            elif choice == "k":
                pprint(the_API)
                input_enter = input("Press enter to go back : ")
                os.system('cls' if os.name == 'nt' else 'clear')
            elif choice in possibilities:
                if choice == "main":
                    main_choice_def(the_API, choice)
                elif choice == "sys":
                    sys_choice_def(the_API, choice)
                elif choice == "wind":
                    wind_choice_def(the_API, choice)
                elif choice == "coord":
                    coord_choice_def(the_API, choice)
                elif choice == "clouds":
                    cloud_choice_def(the_API, choice)
                elif choice == "weather":
                    weather_choice_def(the_API, choice)
                else:
                    print_regel(("input user: {:^" + str(MAX_WORD_LENGTH) + "} output program: {:^" + str(MAX_WORD_LENGTH) + "}").format("[" + choice + "]", the_API[choice]))
                    input_enter = input("Press enter to go back : ")
                    os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("That is not possible. ")
                input_enter = input("Press enter to go back : ")
                os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("That city deosn't exist. ")
        input_enter = input("Press enter to go back : ")
        os.system('cls' if os.name == 'nt' else 'clear')
        runner_code()

runner_code()
