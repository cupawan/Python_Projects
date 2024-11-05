import os
import requests


class OpenCageData:
    def __init__(self):
        self.api_key = os.environ['OPENCAGE_DATA_API_KEY']
        self.base_url = "https://api.opencagedata.com/geocode/v1/json"
    
    def validateInput(self,user_input):
        return user_input.strip()
    
    def geocode(self, user_input):
        params = {
            'q': user_input,
            'key': self.api_key,
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                first_result = data['results'][0]
                latitude = first_result['geometry']['lat']
                longitude = first_result['geometry']['lng']
                formatted_address = first_result['formatted']
                return {'latitude': latitude, 'longitude': longitude, 'formatted_address': formatted_address}
            else:
                raise
        else:
            raise
            
if __name__ == "__main__":
    geocoding_instance = OpenCageData()
    user_input = input("Enter Address: ")
    user_input = geocoding_instance.validateInput(user_input=user_input)
    result = geocoding_instance.geocode(user_input=user_input)
    print(result)


    
