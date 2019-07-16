import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from statsdmetrics import setup_metrics

if __name__ == '__main__':
    sentry_sdk.init(
        dsn="http://203b6ccf1913474ea7a5d2b15c6b58f7@zonar.unboxthepattern.com:9000/3",
        integrations=[FlaskIntegration()]
    )

    # Sentry messages can be manually logged using the base api.
    # More complex types of logging can be done using the Sentry client.
    sentry_sdk.capture_message("Test")

app = Flask(__name__)

if __name__ == '__main__':
    # This line adds statsd performance monitoring to all api calls.
    setup_metrics(app)

@app.route('/')
def index():
    return "Hello World", 200

@app.route('/throwexception')
def throwexception():
    # When this exception is thrown, Sentry will automatically log it thanks to its Flask integration.
    raise ValueError("Something bad happened.")

if __name__ == '__main__':
    app.run(host='0.0.0.0')