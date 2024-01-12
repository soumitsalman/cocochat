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