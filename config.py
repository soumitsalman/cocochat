import os
import json

def get_slack_bot_token() -> str:
    return os.getenv("COCOCHAT_SLACK_BOT_TOKEN")

def get_slack_app_token() -> str:
    return os.getenv("COCOCHAT_SLACK_APP_TOKEN")

def get_slack_signing_secret() -> str:
    return os.getenv("COCOCHAT_SIGNING_SECRET")

def get_llm_service_api_key() -> str:
    return os.getenv("ANYSCALE_API_KEY")

def get_llm_service_base_url() -> str:
    return os.getenv("ANYSCALE_BASE_URL")

def get_llm_chat_model() -> str:
    return os.getenv("LANGUAGE_MODEL")

def get_chat_bot_instructions() -> str:
    return config_file["INSTRUCTION"]

def get_home_page_content() -> str:
    return config_file["HOME_PAGE"]

def load_config_file():
    with open("config.json", 'r') as file:
        return json.load(file)

# these are additional config that are not secrets or deployment time app settings
config_file = load_config_file()