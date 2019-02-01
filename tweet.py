import twitter
import darksky_weather
import config as c

api = twitter.Api(consumer_key=c.twitter_api[0],
                  consumer_secret=c.twitter_api[1],
                  access_token_key=c.twitter_api[2],
                  access_token_secret=c.twitter_api[3])


def degrees_to_cardinal(d):
    dirs = ["Noord", "Noord Noord Oost", "Noord Oost", "Oost Noord Oost", "Oost", "Oost Zuid Oost", "Zuid Oost",
            "Zuid Zuid Oost", "Zuid", "Zuid Zuid West", "Zuid West", "West Zuid West", "West", "West Noord West",
            "Noord West", "Noord Noord West"]
    ix = int((d + 11.25)/22.5)
    return dirs[ix % 16]


weather = darksky_weather.CurrentWeather()

weather_json = weather.fetch_current_weather().json
condition = weather_json['currently']['summary']
temperature = round(int(weather_json['currently']['temperature']))
humidity = int(float(weather_json['currently']['humidity']) * 100)
pressure = int(float(weather_json['currently']['pressure']))
wind_speed = round(int(weather_json['currently']['windSpeed']))
wind_bearing = degrees_to_cardinal(int(weather_json['currently']['windBearing']))


tweet = 'Temperatuur in #Annen: {}\xb0 \nLuchtvochtigheid: {}%\nBarometer: {}hPa\nWind: {}, {}ms'.format(
    temperature, humidity, pressure, wind_bearing, wind_speed)

status = api.PostUpdate(tweet)
