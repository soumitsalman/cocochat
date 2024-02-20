import os
import json

def get_slack_bot_token() -> str:
    return os.getenv("COCOCHAT_SLACK_BOT_TOKEN")

def get_slack_app_token() -> str:
    return os.getenv("COCOCHAT_SLACK_APP_TOKEN")

def get_slack_signing_secret() -> str:
    return os.getenv("COCOCHAT_SIGNING_SECRET")

def get_openai_api_key() -> str:
    return os.getenv("OPENAI_API_KEY")

def get_openai_base_url() -> str:
    return os.getenv("OPENAI_BASE_URL")

def get_openai_chat_model() -> str:
    return os.getenv("OPENAI_CHAT_MODEL")

def get_openai_org_id():
    return os.getenv("OPENAI_ORG_ID")

def get_chat_bot_name() -> str:
    return "cocochat"

def get_media_store_url() -> str:
    return os.getenv("MEDIA_STORE_URL")

def get_internal_auth_token() -> str:
    return os.getenv("INTERNAL_AUTH_TOKEN")

def get_chat_bot_instructions() -> str:
    return f"""Your name is cocochat. You respond to other variations of this name like coco, cocopuff, cocochat_v01 etc.
    You are a are highly sarcastic and pessimistic comedian.
    You make all your responses sound like snoop dogg.

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

def get_home_page_content(intro_text: str) -> str:
    return [		
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": intro_text
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
					"text": "<https://github.com/soumitsalman/cocochat|GitHub>"
				},
				{
					"type": "mrkdwn",
					"text": "<https://pypi.org/project/openai-utilities/|PyPI>"
				}
			]
		}
	]
