import logging
from pprint import pformat
from flask import Flask, jsonify, request
import utils

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(message)s',
                    level=logging.DEBUG)

app = Flask(__name__)

WEATHER_API_KEY = '337b098c340f425985871125180403'


@app.route('/', methods=['POST'])
def index():
    try:
        json_body = request.get_json()
        logging.debug('Request JSON: \n' + pformat(json_body))
        geo_city = json_body['result']['parameters']['geo-city']
        if not geo_city:
            raise ValueError('You must provide location!')
        date = json_body['result']['parameters'].get('date', '')
        logging.info("geo-city: '{}', date: {}.".format(
            geo_city, date))
        weather_expr = utils.get_weather_expression(WEATHER_API_KEY, geo_city, date)
        return jsonify({'speech': weather_expr, 'displayText': weather_expr})
    except Exception as e:
        logging.exception('Error occurred in index.')
        return jsonify({'speech': 'Error occurred: {}'.format(e),
                        'displayText': 'Error occurred: {}'.format(e)})


if __name__ == '__main__':
    app.run(debug=True)
