import os
import csv
import pytz
import requests
import pandas as pd
from datetime import datetime
from DatetimeUtils import CommonUtils



class OpenWeatherMap:
    def __init__(self):
        self.api_key = os.environ['OWM_API_KEY']
        self.time_utils = CommonUtils()
        self.current_weather_base_url = os.environ['OWM_CURRENT_WEATHER_BASE_URL']
        self.geocode_url = os.environ['GEOCODE_URL']

    def save_csv(self, data):
        filepath = os.path.join(self.current_dir, 'Geocoding.csv')
        if not os.path.exists(filepath):
            with open(filepath, 'a+') as data_file:
                csvwriter = csv.writer(data_file)
                csvwriter.writerows([["Address", "Latitude", "Longitude"], data])
        else:
            with open(filepath, 'a+') as data_file:
                csvwriter = csv.writer(data_file)
                csvwriter.writerow(data)

    def geocode(self, address, limit=1):
        params = {'q': address, 'limit' : limit, 'appid' : self.api_key}
        response = requests.get(url=self.geocode_url,params = params).json()[0]
        data = [address, response['lat'], response['lon']]
        self.save_csv(data=data)
        return response['lat'], response['lon']
    
    def request_weather_data(self,lat,lon):
        params = {'lat': lat, 'lon' : lon, 'appid' : self.api_key,'units' : 'metric'}
        response = requests.get(url = self.current_weather_base_url,params=params).json()
        data = response['current']
        vals = [str(self.time_utils.timestamp_to_datetime(data['dt'])),str(self.time_utils.timestamp_to_datetime(data['sunrise'])),str(self.time_utils.timestamp_to_datetime(data['sunset'])),f"{data['temp']}°C",f"{data['feels_like']}°C",f"{data['pressure']}mb",f"{data['humidity']}%",f"{data['dew_point']}°C",str(data["uvi"]),f"{data['clouds']}%",f"{data['visibility']} Metres",f"{data['wind_speed']}m/s",str(data['wind_deg'])]
        return vals
