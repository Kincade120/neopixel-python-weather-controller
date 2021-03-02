
import os
import sys
import board
import neopixel
import configparser
import requests
from datetime import datetime
import time
import json
import threading
import numpy as np

def loadConfig():
    with open('/home/pi/neopixel-controller-python/config.json', 'r') as jsonConfig:
        data = json.load(jsonConfig)
        return data
 
def get_weather(api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?id=3333170&appid={}".format(api_key)
    r = requests.get(url)
    return r.json()

def getTOD():
    now = datetime.now()
    tod = ""
    if now.hour >= 8 and now.hour < 20:
        tod = "day"
    else: 
        tod = "night"
    return tod

def getWeatherDay(weather_type, description, pixels):
    if weather_type == "thunderstorm" or  description == "thunderstorm":
        pixels[0] = (0, 56, 163)
        pixels[1] = (97, 97, 97)
        pixels[2] = (0, 56, 163)
        pixels[3] = (97, 97, 97)
        pixels[4] = (0, 56, 163)
        pixels[5] = (97, 97, 97)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    elif weather_type == "drizzle" or  description == "drizzle":
        pixels[0] = (101, 184, 247)
        pixels[1] = (191, 191, 191)
        pixels[2] = (101, 184, 247)
        pixels[3] = (191, 191, 191)
        pixels[4] = (101, 184, 247)
        pixels[5] = (191, 191, 191)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    elif weather_type == "rain" or  description == "rain":
        pixels[0] = (148, 185, 255)
        pixels[1] = (191, 191, 191)
        pixels[2] = (148, 185, 255)
        pixels[3] = (191, 191, 191)
        pixels[4] = (148, 185, 255)
        pixels[5] = (191, 191, 191)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    elif weather_type == "snow" or  description == "snow":
        pixels[0] = (237, 237, 237)
        pixels[1] = (237, 237, 237)
        pixels[2] = (237, 237, 237)
        pixels[3] = (191, 191, 191)
        pixels[4] = (191, 191, 191)
        pixels[5] = (191, 191, 191)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    elif weather_type == "mist" or  description == "mist":
        pixels[0] = (181, 181, 181)
        pixels[1] = (181, 181, 181)
        pixels[2] = (181, 181, 181)
        pixels[3] = (0, 149, 255)
        pixels[4] = (5, 140, 237)
        pixels[5] = (4, 128, 217)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    elif weather_type == "smoke" or  description == "smoke":
        pixels[0] = (117, 117, 117)
        pixels[1] = (117, 117, 117)
        pixels[2] = (117, 117, 117)
        pixels[3] = (117, 117, 117)
        pixels[4] = (117, 117, 117)
        pixels[5] = (117, 117, 117)
        pixels[6] = (117, 117, 117)
        pixels[7] = (117, 117, 117)
    elif weather_type == "haze" or  description == "haze":
        pixels[0] = (117, 117, 117)
        pixels[1] = (117, 117, 117)
        pixels[2] = (117, 117, 117)
        pixels[3] = (117, 117, 117)
        pixels[4] = (117, 117, 117)
        pixels[5] = (117, 117, 117)
        pixels[6] = (117, 117, 117)
        pixels[7] = (117, 117, 117)
    elif weather_type == "dust" or  description == "dust":
        pixels[0] = (140, 140, 140)
        pixels[1] = (140, 140, 140)
        pixels[2] = (140, 140, 140)
        pixels[3] = (140, 140, 140)
        pixels[4] = (140, 140, 140)
        pixels[5] = (140, 140, 140)
        pixels[6] = (140, 140, 140)
        pixels[7] = (140, 140, 140)
    elif weather_type == "fog" or  description == "fog":
        pixels[0] = (181, 181, 181)
        pixels[1] = (181, 181, 181)
        pixels[2] = (181, 181, 181)
        pixels[3] = (0, 149, 255)
        pixels[4] = (5, 140, 237)
        pixels[5] = (4, 128, 217)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    elif weather_type == "sand" or  description == "sand":
        pixels[0] = (235, 220, 61)
        pixels[1] = (235, 220, 61)
        pixels[2] = (235, 220, 61)
        pixels[3] = (235, 220, 61)
        pixels[4] = (235, 220, 61)
        pixels[5] = (235, 220, 61)
        pixels[6] = (235, 220, 61)
        pixels[7] = (235, 220, 61)
    elif weather_type == "ash" or  description == "ash":
        pixels[0] = (140, 140, 140)
        pixels[1] = (140, 140, 140)
        pixels[2] = (140, 140, 140)
        pixels[3] = (140, 140, 140)
        pixels[4] = (140, 140, 140)
        pixels[5] = (140, 140, 140)
        pixels[6] = (140, 140, 140)
        pixels[7] = (140, 140, 140)
    elif weather_type == "squalls" or  description == "squalls":
        pixels[0] = (0, 36, 145)
        pixels[1] = (0, 36, 145)
        pixels[2] = (0, 36, 145)
        pixels[3] = (0, 36, 145)
        pixels[4] = (0, 36, 145)
        pixels[5] = (0, 36, 145)
        pixels[6] = (0, 36, 145)
        pixels[7] = (0, 36, 145)
    elif weather_type == "tornado" or  description == "tornado":
        pixels[0] = (207, 0, 0)
        pixels[1] = (207, 0, 0)
        pixels[2] = (207, 0, 0)
        pixels[3] = (207, 0, 0)
        pixels[4] = (207, 0, 0)
        pixels[5] = (207, 0, 0)
        pixels[6] = (207, 0, 0)
        pixels[7] = (207, 0, 0)
    elif weather_type == "clear sky" or  description == "clear sky":
        pixels[0] = (0, 149, 255)
        pixels[1] = (0, 149, 255)
        pixels[2] = (0, 149, 255)
        pixels[3] = (0, 149, 255)
        pixels[4] = (5, 140, 237)
        pixels[5] = (4, 128, 217)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    elif weather_type == "clouds" or  description == "clouds":
        pixels[0] = (0, 149, 255)
        pixels[1] = (0, 149, 255)
        pixels[2] = (0, 149, 255)
        pixels[3] = (186, 186, 186)
        pixels[4] = (186, 186, 186)
        pixels[5] = (186, 186, 186)
        pixels[6] = (255, 196, 0)
        pixels[7] = (186, 186, 186)
    else:
        pixels[0] = (0, 149, 255)
        pixels[1] = (0, 149, 255)
        pixels[2] = (0, 149, 255)
        pixels[3] = (0, 149, 255)
        pixels[4] = (5, 140, 237)
        pixels[5] = (4, 128, 217)
        pixels[6] = (255, 196, 0)
        pixels[7] = (2, 100, 171)
    return pixels

def getWeatherNight(weather_type, description, pixels):
    if weather_type == "thunderstorm" or  description == "thunderstorm":
        pixels[0] = (0, 56, 163)
        pixels[1] = (97, 97, 97)
        pixels[2] = (0, 56, 163)
        pixels[3] = (97, 97, 97)
        pixels[4] = (0, 56, 163)
        pixels[5] = (97, 97, 97)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)
    elif weather_type == "drizzle" or  description == "drizzle":
        pixels[0] = (101, 184, 247)
        pixels[1] = (191, 191, 191)
        pixels[2] = (101, 184, 247)
        pixels[3] = (191, 191, 191)
        pixels[4] = (101, 184, 247)
        pixels[5] = (191, 191, 191)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)
    elif weather_type == "rain" or  description == "rain":
        pixels[0] = (148, 185, 255)
        pixels[1] = (191, 191, 191)
        pixels[2] = (148, 185, 255)
        pixels[3] = (191, 191, 191)
        pixels[4] = (148, 185, 255)
        pixels[5] = (191, 191, 191)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)
    elif weather_type == "snow" or  description == "snow":
        pixels[0] = (237, 237, 237)
        pixels[1] = (237, 237, 237)
        pixels[2] = (237, 237, 237)
        pixels[3] = (191, 191, 191)
        pixels[4] = (191, 191, 191)
        pixels[5] = (191, 191, 191)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)
    elif weather_type == "mist" or  description == "mist":
        pixels[0] = (181, 181, 181)
        pixels[1] = (181, 181, 181)
        pixels[2] = (181, 181, 181)
        pixels[3] = (227, 142, 5)
        pixels[4] = (194, 120, 2)
        pixels[5] = (150, 95, 8)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)
    elif weather_type == "smoke" or  description == "smoke":
        pixels[0] = (117, 117, 117)
        pixels[1] = (117, 117, 117)
        pixels[2] = (117, 117, 117)
        pixels[3] = (117, 117, 117)
        pixels[4] = (117, 117, 117)
        pixels[5] = (117, 117, 117)
        pixels[6] = (117, 117, 117)
        pixels[7] = (117, 117, 117)
    elif weather_type == "haze" or  description == "haze":
        pixels[0] = (117, 117, 117)
        pixels[1] = (117, 117, 117)
        pixels[2] = (117, 117, 117)
        pixels[3] = (117, 117, 117)
        pixels[4] = (117, 117, 117)
        pixels[5] = (117, 117, 117)
        pixels[6] = (117, 117, 117)
        pixels[7] = (117, 117, 117)
    elif weather_type == "dust" or  description == "dust":
        pixels[0] = (140, 140, 140)
        pixels[1] = (140, 140, 140)
        pixels[2] = (140, 140, 140)
        pixels[3] = (140, 140, 140)
        pixels[4] = (140, 140, 140)
        pixels[5] = (140, 140, 140)
        pixels[6] = (140, 140, 140)
        pixels[7] = (140, 140, 140)
    elif weather_type == "fog" or  description == "fog":
        pixels[0] = (181, 181, 181)
        pixels[1] = (181, 181, 181)
        pixels[2] = (181, 181, 181)
        pixels[3] = (227, 142, 5)
        pixels[4] = (194, 120, 2)
        pixels[5] = (150, 95, 8)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)
    elif weather_type == "sand" or  description == "sand":
        pixels[0] = (235, 220, 61)
        pixels[1] = (235, 220, 61)
        pixels[2] = (235, 220, 61)
        pixels[3] = (235, 220, 61)
        pixels[4] = (235, 220, 61)
        pixels[5] = (235, 220, 61)
        pixels[6] = (235, 220, 61)
        pixels[7] = (235, 220, 61)
    elif weather_type == "ash" or  description == "ash":
        pixels[0] = (140, 140, 140)
        pixels[1] = (140, 140, 140)
        pixels[2] = (140, 140, 140)
        pixels[3] = (140, 140, 140)
        pixels[4] = (140, 140, 140)
        pixels[5] = (140, 140, 140)
        pixels[6] = (140, 140, 140)
        pixels[7] = (140, 140, 140)
    elif weather_type == "squalls" or  description == "squalls":
        pixels[0] = (0, 36, 145)
        pixels[1] = (0, 36, 145)
        pixels[2] = (0, 36, 145)
        pixels[3] = (0, 36, 145)
        pixels[4] = (0, 36, 145)
        pixels[5] = (0, 36, 145)
        pixels[6] = (0, 36, 145)
        pixels[7] = (0, 36, 145)
    elif weather_type == "tornado" or  description == "tornado":
        pixels[0] = (207, 0, 0)
        pixels[1] = (207, 0, 0)
        pixels[2] = (207, 0, 0)
        pixels[3] = (207, 0, 0)
        pixels[4] = (207, 0, 0)
        pixels[5] = (207, 0, 0)
        pixels[6] = (207, 0, 0)
        pixels[7] = (207, 0, 0)
    elif weather_type == "clear sky" or  description == "clear sky":
        pixels[0] = (255, 159, 5)
        pixels[1] = (255, 159, 5)
        pixels[2] = (9, 1, 74)
        pixels[3] = (9, 1, 74)
        pixels[4] = (9, 1, 74)
        pixels[5] = (9, 1, 74)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)
    elif weather_type == "clouds" or  description == "clouds":
        pixels[0] = (255, 159, 5)
        pixels[1] = (255, 159, 5)
        pixels[2] = (255, 159, 5)
        pixels[3] = (186, 186, 186)
        pixels[4] = (186, 186, 186)
        pixels[5] = (186, 186, 186)
        pixels[6] = (237, 237, 237)
        pixels[7] = (186, 186, 186)
    else:
        pixels[0] = (255, 159, 5)
        pixels[1] = (255, 159, 5)
        pixels[2] = (9, 1, 74)
        pixels[3] = (9, 1, 74)
        pixels[4] = (9, 1, 74)
        pixels[5] = (9, 1, 74)
        pixels[6] = (237, 237, 237)
        pixels[7] = (9, 1, 74)

    return pixels

def weather(pixels, api_key, refreshTime):
    weather = get_weather(api_key)
    time_of_day  = getTOD()
    now = datetime.now()
    main_type = weather['weather'][0]['main'].lower()
    print(main_type)
    description = weather['weather'][0]['description'].lower()
    if time_of_day == "day":
        pixels = getWeatherDay(main_type, description, pixels)            
    elif time_of_day == "night":
        pixels = getWeatherNight(main_type, description, pixels)
    pixels.show()
    time.sleep(float(refreshTime))


def breathe(pixels, breatheTimeDay, breatheTimeNight):
    brightnessValues = np.arange(0.0, 0.5, 0.01)
    while True:
        time_of_day  = getTOD()
        if time_of_day == "day":
            for value in brightnessValues:
                pixels.brightness = value
                pixels.show()
                time.sleep(float(breatheTimeDay))
            for valueR in reversed(brightnessValues):
                pixels.brightness = valueR
                pixels.show()
                time.sleep(float(breatheTimeDay))
        elif time_of_day == "night":
            for value in brightnessValues:
                pixels.brightness = value
                pixels.show()
                time.sleep(float(breatheTimeNight))
            for valueR in reversed(brightnessValues):
                pixels.brightness = valueR
                pixels.show()
                time.sleep(float(breatheTimeNight))

def main():
    try:
        config = loadConfig()
        api_key = config["openweathermap"]["api"]
        pixels = neopixel.NeoPixel(board.D18, 8, brightness=0.5, auto_write=False, pixel_order=neopixel.GRB)
        refreshTime = config["timers"]["refreshTime"]
        breatheTimeDay = config["timers"]["breatheTimeDay"]
        breatheTimeNight = config["timers"]["breatheTimeNight"]
        threading.Timer(1, breathe, args=[pixels, breatheTimeDay, breatheTimeNight] ).start()
        while True:
            weather(pixels, api_key, refreshTime)
            

        
    except KeyboardInterrupt:
        pass
    except ValueError as err:
        print(f"Error: {err}")
    except KeyError as err:
        print(f"Error: Please ensure the {err} environment variable is set")

if __name__ == "__main__":
    main()