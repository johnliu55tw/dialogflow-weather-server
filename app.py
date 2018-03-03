from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    q_response = 'This is a sample response from your webhook!'
    resp = {'speech': q_response, 'displayText': q_response}
    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)
