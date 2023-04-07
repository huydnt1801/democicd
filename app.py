from flask import Flask

app = Flask(__name__)


@app.route('/health/live')
def health_liveness():
    return '', 200


@app.route('/health/ready')
def health_readiness():
    return '', 200


@app.route('/')
def hello_world():
    return "Hello World very new"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
