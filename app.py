# this can run on either SOCKET mode or HTTP mode
import slack_receiver
from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

# running in HTTP mode
app = Flask(__name__)
handler = SlackRequestHandler(slack_receiver.app)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    app.run(port=8000)

# uncomment the following to run in SOCKET mode
# import config
# from slack_bolt.adapter.socket_mode import SocketModeHandler      
# app = SocketModeHandler(slack_receiver.app, config.get_slack_app_token())
# if __name__ == "__main__":
#     app.start()


    