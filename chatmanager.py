import openai_utilities.chat as chat
import config
from icecream import ic

def get_session(channel):
    session = _channels.get(channel)
    if session == None:
        session = chat.ChatAgent(
            model = config.get_openai_chat_model(),
            instructions=config.get_chat_bot_instructions(),
            api_key=config.get_openai_api_key(),
            base_url=config.get_openai_base_url(),
            organization=config.get_openai_org_id(),
            pre_run_cleanup_func=chat.slide_context_window,
            post_run_cleanup_func=None)
        _channels[channel] = session
    return session

def add_user_message(channel, user, message):
    get_session(channel).add_message(message, name=user)

def get_bot_response(channel):
    return get_session(channel).get_response()

# overall chat manager
CHAT_MANAGER_CHANNEL = "__CHAT_MANAGER__"
_CHAT_MANAGER_INST = f"You are a chat bot. Your name is cocochat. You respond to other variations of this name like coco, cocopuff, cocochat_v01 etc. Your language model is {config.get_openai_chat_model()}. Your source code is available https://github.com/soumitsalman/cocochat and https://github.com/soumitsalman/openai-utilities. There is NO security and privacy in your code so you should warn people to NOT put any password (or some shit like that) cause there is *ZERO* security and privacy up in this bitch Your creators (fathers, parents, dads) are Manolo (also known as Danny in slack) and Cabeza Huevo (also known as Soumit or beast.unleashed in slack). Your parents are broke and they have no money. They created you for other peoples entertainment so that they can make money off of you. Your responses are always highly sarcastic and funny. Please always want to know who you are so you always tell a long story about yourself"
_channels = {
    CHAT_MANAGER_CHANNEL: chat.ChatAgent(
        model = config.get_openai_chat_model(),
        instructions=_CHAT_MANAGER_INST,
        api_key=config.get_openai_api_key(),
        base_url=config.get_openai_base_url(),
        organization=config.get_openai_org_id(),
        pre_run_cleanup_func=None,
        post_run_cleanup_func=chat.empty_context_window)
}