import pydarksky
import config as c
from datetime import timedelta, datetime


class DarkSkyApi(object):

    def __init__(self):
        self.api_key = c.darksky_api[0]
        self.annen = (float(c.darksky_api[1]), float(c.darksky_api[2]))
        self.client = pydarksky.DarkSky(api_key=self.api_key)
        self.client.lang = 'Dutch'
        self.client.units = 'si'


class TimeMachine(DarkSkyApi):

    def fetch_time_machine_weather(self, single_date):
        resp = self.client.weather(latitude=self.annen[0], longitude=self.annen[1], date=datetime(int(single_date[0]),
                                                                                                  int(single_date[1]),
                                                                                                  int(single_date[2]))
                                   )
        data = resp.json['daily']['data'][0]
        r = data['time'], data['icon'], data['summary'], data['temperatureMax'], data['temperatureMin']
        print(r)

    def fetch_period(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            single_date = start_date + timedelta(n)
            single_date = str(single_date).split('-')
            self.fetch_time_machine_weather(single_date)


class CurrentWeather(DarkSkyApi):

    def fetch_current_weather(self):
        resp = self.client.weather(latitude=self.annen[0], longitude=self.annen[1])
        return resp
