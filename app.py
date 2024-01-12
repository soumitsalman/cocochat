from slack_app import bolt_app

# code for production deployment in azure app service
from flask import Flask, request
app = Flask(__name__)

from slack_bolt.adapter.flask import SlackRequestHandler
handler = SlackRequestHandler(bolt_app)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# start the app
if __name__ == "__main__":
    app.run(port = 8000)