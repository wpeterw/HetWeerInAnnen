# -*- coding: utf-8 -*-

import tweepy
import config as c
from retrieve_weather import OpenWeatherMap

current_weather = OpenWeatherMap()


class Tweet:
    def __init__(self):
        self.consumer_key = c.consumer_key
        self.consumer_secret = c.consumer_secret
        self.access_token = c.access_token
        self.access_token_secret = c.access_token_secret
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    @staticmethod
    def create_tweet():
        weather = current_weather.parse_weather()
        temperature = weather['temperature']
        degrees = '\u2103 '
        condition = weather['condition']
        humidity = weather['humidity']
        pressure = weather['pressure']
        wind_direction = weather['wind_direction']
        wind_speed = weather['wind_speed']
        rain = weather['rain']

        tweet = 'Temperatuur in #Annen: {temperature}{degrees}' \
                '{condition}. \n' \
                'Luchtvochtigheid: {humidity}% \n' \
                'Barometer: {pressure}hpa \n' \
                'Wind: {direction}, {speed} bft\n' \
                'Neerslag: {rain} mm'.format(temperature=temperature,
                                             degrees=degrees,
                                             condition=condition,
                                             humidity=humidity,
                                             pressure=pressure,
                                             direction=wind_direction,
                                             speed=wind_speed,
                                             rain=rain)
        return tweet

    def send_tweet(self, tweet):
        self.api.update_status(tweet)
