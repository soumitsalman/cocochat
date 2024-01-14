from openai_connectors.chat_connector import OpenAIChatSession
import config
from icecream import ic

channels = {}

def get_session(channel):
    session = channels.get(channel)
    if session == None:
        session = OpenAIChatSession(
            model = config.get_llm_chat_model(),
            instruction=config.get_chat_bot_instructions(),
            service_api_key=config.get_llm_service_api_key(),
            service_url=config.get_llm_service_base_url())
        channels[channel] = session
    return session

def queue_user_message(channel, user, message):
    get_session(channel).add_to_thread(message, name=user)
    ic("added to " + channel)

def get_response(channel):
    return get_session(channel).run_thread()
