from openai_connectors.chat_connector import OpenAIChatSession
import config
from icecream import ic

channels = {}

def get_session(channel):
    session = channels.get(channel)
    if session == None:
        session = OpenAIChatSession(
            model = config.get_llm_service_model(),
            instructions=config.get_chat_bot_instructions(),
            api_key=config.get_llm_service_api_key(),
            base_url=config.get_llm_service_base_url())
        channels[channel] = session
    return session

def queue_user_message(channel, user, message):
    get_session(channel).add_to_thread(message, name=user)

def get_response(channel):
    return get_session(channel).run_thread()
    # return "FAKE RESPONSE @beast.unleashed in #cocochat_testing cause #yolo"

def switch_model(channel, model):    
    try:
        get_session(channel).update_model(model)
        return True
    except:
        return False