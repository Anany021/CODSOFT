import tkinter as tk
import requests
from tkinter import font

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(weather_data):
    city_name = weather_data["name"]
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    weather_desc = weather_data["weather"][0]["description"]

    result_label.config(text=f"City: {city_name}\n"
                             f"Temperature: {temp} °C\n"
                             f"Humidity: {humidity} %\n"
                             f"Wind Speed: {wind_speed} m/s\n"
                             f"Weather: {weather_desc}")

def get_weather():
    location = location_entry.get()
    try:
        weather_data = get_weather_data(api_key, location)
        display_weather(weather_data)
    except requests.exceptions.RequestException:
        result_label.config(text="Error: Could not retrieve weather data.\n"
                                 "Please check your internet connection.")
    except KeyError:
        result_label.config(text="Error: Could not find weather data for the specified location.")
    except Exception as e:
        result_label.config(text=f"An unexpected error occurred: {e}")

# Set your OpenWeatherMap API key here
api_key = "dcd503106b32198e81cbc037a7031fad"

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("300x300")
# Create and place widgets
label_font=font.Font(weight='bold')
location_label = tk.Label(root, text="Enter city or zip code:", bg='dark blue', fg='yellow', font=label_font)
location_label.pack(pady=10)

location_entry = tk.Entry(root)
location_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather ,bg='dark blue',fg='yellow',font=label_font)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=300,bg='Dark Blue',fg='yellow',font=label_font)
result_label.pack()
root.configure(bg='Dark Blue')
# Start the GUI event loop
root.mainloop()

