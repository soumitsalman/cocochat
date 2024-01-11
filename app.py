import os
import config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# set up the initial app
app = App(
    token=config.get_slack_bot_token(),
    signing_secret=config.get_slack_signing_secret()
)

@app.message("ping")
def respond_ping(message, say):
    resp = f"Pong to <@{message['user']}>"
    print(resp)
    say(resp)

def start_app():
    app.start(port = 8000)


# start the slack app
if __name__ == "__main__":
    start_app()