import requests
from dotenv import load_dotenv
import os
def weather(place):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={place}")
    data = response.json()
    status = response.status_code
    if(status==200):
    # Weather inputs
        temp = data["current"].get("temp_c")
        condition = data["current"]["condition"].get("text")
        humidity = data["current"].get("humidity")
        last_updated = data["current"].get("last_updated")

        def dayornight():
            diurnal = ""
            if(data["current"].get("is_day")==0):
                diurnal = "Night"
            elif(data["current"].get("is_day")==1):
                diurnal = "Day"

            return diurnal

        diu = dayornight()
    
        weatherdata =  f"Showing temperature for {data["location"].get("name")}, {data["location"].get("region")}, {data["location"].get("country")}\ntemprature: {temp}\ncondition: {condition}\nhumidity: {humidity}\nDiural_cycle: {diu}\nlast updated on {last_updated}"
        return weatherdata

    