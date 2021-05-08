from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('b4898de25340a574ce43d9b2fa78664f')
mgr = owm.weather_manager()
input_city = input("What city you are interested: ")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(input_city)
w = observation.weather


wind_speed = w.wind()["speed"]                # {'speed': 4.6, 'deg': 330}
humidity = w.humidity               # 87
temperature = w.temperature('celsius')["temp"] # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
temperature_max = w.temperature("celsius")["temp_max"]
temperature_min = w.temperature("celsius")["temp_min"]
rain = w.rain                    # {}
w.heat_index             # None
w.clouds                  # 75

print(f"In {input_city} wind is: {wind_speed} m/s")
print(f"In {input_city} humidity is: {humidity}%" )
print(f"In {input_city} temperature is {temperature} degrees by celsius")
print(f"In {input_city} max temperature is {temperature_max} degrees by celsius")
print(f"In {input_city} ming temperature is {temperature_min} degrees by celsius")

