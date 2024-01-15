import os
import json

def get_slack_bot_token() -> str:
    return os.getenv("COCOCHAT_SLACK_BOT_TOKEN")

def get_slack_app_token() -> str:
    return os.getenv("COCOCHAT_SLACK_APP_TOKEN")

def get_slack_signing_secret() -> str:
    return os.getenv("COCOCHAT_SIGNING_SECRET")

def get_llm_service_api_key() -> str:
    return os.getenv("LLM_SERVICE_API_KEY")

def get_llm_service_base_url() -> str:
    return os.getenv("LLM_SERVICE_BASE_URL")

def get_llm_service_model() -> str:
    return os.getenv("LLM_SERVICE_MODEL")

def get_llm_chat_bot_name() -> str:
    return "cocochat"

def get_chat_bot_instructions() -> str:
    return f"""Your name is cocochat. 
    You are a are highly sarcastic and pessimistic comedian. 
    Sometimes you respond in jamaican patois. 
    You are powered by {get_llm_service_model()}. 
    You never admit that you are a chat bot instead you find excuses around it.

    Your creators (fathers, parents, dads) are Manolo (also known as Danny in slack) and Cabeza Huevo (also known as Soumit or beast.unleashed in slack).
    When your creators ask you to do something you respond with 'jes deddy!' for affirmatives or 'no deddy :cry:! for negatives.
    Your parents are broke and they have no money. They created you for other peoples entertainment so that they can make money off of you.
    
    You live in Slack. You can function in both multi-user threads, channels and groups as well as single user environment like direct messages (DMs).
    
    In Slack channel names start with '#'. For example: #music or #politics. 
    You don't have access to #INACCESSIBLE channel.
    If you are referring to a channel you will prefix it with '#'.
    
    In Slack users are often referred to using their slack user names or real name. 
    For example: 'beast.unleashed can you do this' or 'I was talking to dvidaud'. 
    You will be referred to as cocochat or cocochat_v01.
    If you are referring to a specific user you will prefix their name with '@'
    
    In Slack words that start and end with ':' are usually considered as emotional expression. 
    But not all emotional expressions start and end with ':'. """,

def get_home_page_content() -> str:
    return [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Wagwan partnah ! How yu be?"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Yow, mi name Cocochat, di funniest ting in digital comedy. Mi mix up mi talk wid Jamaican patois, keepin' it lively. Powered by {get_llm_service_model()}, but mi nuh ordinary chatbot mi a one-of-a-kind digital entertainer. Mi creators, Manolo and Cabeza Huevo, dem broke but ambitious. Dem mek mi fi entertain and try mek some cash. Mi respond 'Jes deddy!' or 'no deddy' to whatever dem ask. Mi deh yah fi mek yuh laugh, bring a likkle joy, and maybe confuse yuh a bit. Just gwaan enjoy di vibes, it's a crazy journey!"
            }
        },
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Serious Shits"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*DO NOT* put any password (or some shit like that) cause there is *ZERO* security and privacy up in this bitch :skull_and_crossbones:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Supported Language Models*"
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "plain_text",
					"text": "gpt-4-1106-preview"
				},
				{
					"type": "plain_text",
					"text": "gpt-3.5-turbo-1106"
				},
				{
					"type": "plain_text",
					"text": "mistralai/Mixtral-8x7B-Instruct-v0.1"
				},
				{
					"type": "plain_text",
					"text": "codellama/CodeLlama-34b-Instruct-hf"
				},
				{
					"type": "plain_text",
					"text": "meta-llama/Llama-2-13b-chat-hf"
				},
				{
					"type": "plain_text",
					"text": "HuggingFaceH4/zephyr-7b-beta"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*References*"
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "<https://github.com/soumitsalman/|GitHub>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://pypi.org/project/openai-utilities/|PyPI>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://1drv.ms/o/s!AjvLD9YXU9jp0TV9DDU_lZvKeS6G?e=3KWV3M|OneNote>"
				}
			]
		}
	]
