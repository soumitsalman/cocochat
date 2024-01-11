import os

def get_slack_bot_token() -> str:
    return os.getenv("COCOCHAT_SLACK_BOT_TOKEN")

def get_slack_app_token() -> str:
    return os.getenv("COCOCHAT_SLACK_APP_TOKEN")

def get_slack_signing_secret() -> str:
    return os.getenv("COCOCHAT_SIGNING_SECRET")
