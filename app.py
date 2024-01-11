import os
import config
from slack_bolt import App


# set up the initial app
bolt_app = App(
    token=config.get_slack_bot_token(),
    signing_secret=config.get_slack_signing_secret()
)

@bolt_app.message("ping")
def respond_ping(message, say):
    resp = f"Pong to <@{message['user']}>"
    print(resp)
    say(resp)

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