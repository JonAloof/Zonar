import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="http://5f20a399172749bea73d2d0ed7556fe5@zonar.unboxthepattern.com:9000/2",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')