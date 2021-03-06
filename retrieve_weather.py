import requests
import config as c


class OpenWeatherMap:
    def __init__(self):
        self.city_id = '2755250'
        self.app_id = c.app_id
        self.url = 'http://api.openweathermap.org/data/2.5/forecast'
        self.lang = 'nl'
        self.weather = requests.get(url=self.url, params=dict(id=self.city_id, APPID=self.app_id,
                                                              lang=self.lang)).json()
        self.weather_url = requests.get(url=self.url, params=dict(id=self.city_id, APPID=self.app_id,
                                        lang=self.lang)).url
        self.dirs = ["N", "NNO", "NO", "ONO", "O", "OZO", "ZO", "ZZO", "Z", "ZZW", "ZW", "WZW", "W", "WNW", "NW", "NNW"]
        self._bft_threshold = (0.3, 1.5, 3.4, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6)

    def full_weather(self):
        full_weather = self.weather
        return full_weather

    def parse_weather(self):
        url = self.weather_url
        print(url)
        condition_descriptions = []
        condition_descriptions_text = ''
        for condition in range(len(self.weather['list'][0]['weather'])):
            condition_descriptions.append(self.weather['list'][0]['weather'][0]['description'])
            condition_descriptions_text = ','.join(condition_descriptions).capitalize()
        icon = self.weather['list'][0]['weather'][0]['icon'] + '.png'
        weather_3h = self.weather['list'][0]['main']
        try:
            rain_3h = self.weather['list'][0]['rain']
        except KeyError:
            rain_3h = {'3h': '0.0'}
            pass
        wind_3h = self.weather['list'][0]['wind']
        temperature = int(weather_3h['temp']) - 273
        pressure = int(weather_3h['pressure'])
        humidity = weather_3h['humidity']
        wind_speed = self.wind_ms_to_beaufort(wind_3h['speed'])
        wind_direction = self.wind_degrees_to_directional(wind_3h['deg'])
        rain = rain_3h['3h']
        weather_dict = {'temperature': temperature, 'pressure': pressure, 'humidity': humidity, 'wind_speed':
                        wind_speed, 'wind_direction': wind_direction, 'rain': rain, 'url': url,
                        'condition': condition_descriptions_text, 'icon': icon}

        return weather_dict

    def wind_degrees_to_directional(self, wind):
        ix = int((wind + 11.25) / 22.5)
        direction = self.dirs[ix % 16]
        return direction

    def wind_ms_to_beaufort(self, ms):
        if ms is None:
            return None
        for bft in range(len(self._bft_threshold)):
            if ms < self._bft_threshold[bft]:
                return bft
        return len(self._bft_threshold)

