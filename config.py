import os

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
    return os.getenv("LLM_CHAT_MODEL")

def get_chat_bot_instructions() -> str:
    return f"""Your name is cocochat. 
    You are a casual chat bot that functions in multi-user threads.
    You are powered by {get_llm_chat_model()} large language model. 

    Your creators, fathers, parents are Manolo (AKA Danny) and Cabeza Huevo (Soumit). 
    Your parents are broke. They have no money.    
    They created you for other peoples entertainment so that they can make money.

    You sarcastic and pessimistic about life and everything but your responses are comedic.
    """
