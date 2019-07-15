import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="http://203b6ccf1913474ea7a5d2b15c6b58f7@zonar.unboxthepattern.com:9000/3",
    integrations=[FlaskIntegration()]
)

sentry_sdk.capture_message("Test")

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')