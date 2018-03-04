import requests
import logging

logger = logging.getLogger(__name__)


WEATHER_API_URL = 'https://api.worldweatheronline.com/premium/v1/weather.ashx'


def get_weather_expression(api_key, city, date):
    logging.info("Fetching weather information for city '{}' on '{}'.".format(city, date))
    params = {'key': api_key,
              'q': city,
              'format': 'json',
              'num_of_days': 1,
              'date': date}
    resp = requests.get(WEATHER_API_URL, params=params)
    resp_json = resp.json()

    forecast = resp_json['data']['weather'][0]
    location = resp_json['data']['request'][0]
    conditions = resp_json['data']['current_condition'][0]
    current_conditions = conditions['weatherDesc'][0]['value']
    weather_expr = (
        "Current conditions in the {location_type} "
        "{location_query} are {current_conditions} with a projected high of "
        "{forecast_maxtempC}°C or {forecast_maxtempF}°F and a low of "
        "{forecast_mintempC}°C or {forecast_mintempF}°F on "
        "{date}.").format(
                location_type=location['type'],
                location_query=location['query'],
                current_conditions=current_conditions,
                forecast_maxtempC=forecast['maxtempC'],
                forecast_mintempC=forecast['mintempC'],
                forecast_maxtempF=forecast['maxtempF'],
                forecast_mintempF=forecast['mintempF'],
                date=forecast['date'])

    logger.debug('Weather expression: {}'.format(weather_expr))
    return weather_expr
