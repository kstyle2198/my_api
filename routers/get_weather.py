from fastapi import APIRouter
from config import get_secret
from fastapi.encoders import jsonable_encoder
import requests
from geopy.geocoders import Nominatim
import geocoder


router = APIRouter()

g = geocoder.ip('me')
TARGET_CITY = g.city
WEATHER_API = get_secret("OPEN_WEATHER_API")
OPEN_WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/"
GET_GMTPLUS_TIME = "http://worldtimeapi.org/api/timezone/"

@router.get("/weatherInterface", tags=["날씨/위치/시간"])
async def get_weatherInfo():

    regionName = TARGET_CITY

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(regionName)
    print(getLoc)
    lat = str(getLoc.latitude)
    lon = str(getLoc.longitude)

    targetUrl = OPEN_WEATHER_BASE_URL + "weather?lat=" + \
        lat + "&lon=" + lon + "&appid=" + WEATHER_API
    response = requests.get(targetUrl)
    # print(response)
    weather = response.json()['weather'][0]['main']
    country = response.json()['sys']['country']
    # print(weather, country)

    area_name = g.raw["timezone"]

    print(area_name)
    targetUrl = GET_GMTPLUS_TIME + area_name
    # print(targetUrl)

    response = requests.get(targetUrl)
    plusTime = response.json()['raw_offset']
    dateTime = response.json()['datetime']

    result = []
    result.append(["regionname", regionName])
    result.append(["time", plusTime])
    result.append(["time", dateTime])
    result.append(["weather", weather])
    return jsonable_encoder(result)
