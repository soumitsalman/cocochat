# this can run on either SOCKET mode or HTTP mode
import slack_receiver
from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt.adapter.socket_mode import SocketModeHandler
import config

# this can run on either SOCKET mode or HTTP mode
# socket mode requires that in the slack app management portal "Socket Mode" is turned on
MODE = "HTTP" # "SOCKET"


# app = Flask(__name__)
# handler = SlackRequestHandler(bolt_app)

# @app.route("/slack/events", methods=["POST"])
# def slack_events():
#     return handler.handle(request)

# start the app
if __name__ == "__main__":
    if MODE == "HTTP":
        # HTTP mode is powered by flask
        app = Flask(__name__)
        handler = SlackRequestHandler(slack_receiver.app)

        @app.route("/slack/events", methods=["POST"])
        def slack_events():
            return handler.handle(request)
        
        app.run(port=8000)

    else: # MODE == "SOCKET"        
        handler = SocketModeHandler(slack_receiver.app, config.get_slack_app_token())
        handler.start()
