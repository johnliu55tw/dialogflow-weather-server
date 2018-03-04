import logging
from flask import Flask, jsonify, request
import utils

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s:%(message)s',
                    level=logging.DEBUG)

app = Flask(__name__)

WEATHER_API_KEY = '337b098c340f425985871125180403'


@app.route('/', methods=['POST'])
def index():
    logging.info('Query parameters: {}'.format(request.args))
    logging.info('Query JSON body: {}'.format(request.get_json()))

    q_response = 'This is a sample response from your webhook!'
    resp = {'speech': q_response, 'displayText': q_response}
    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)
