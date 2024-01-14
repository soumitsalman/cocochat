import config
from icecream import ic
from slack_bolt import App
from chatsessions import queue_user_message, get_response


# set up the initial app
app = App(
    token=config.get_slack_bot_token(),
    signing_secret=config.get_slack_signing_secret()
)

@app.message()
def receive_message(message, say, client): 
    new_message(
        message_or_event = message, 
        needs_response=message['channel_type'] == "im", # in a DM the conversation is usually ping pong, so respond
        say = say, 
        slack_client = client, 
    )

@app.event("app_mention")
def receive_mention(event, say, client):
    ic(event)
    new_message(
        message_or_event = event,
        needs_response=True, # always respond when mentioned
        say=say, 
        slack_client=client
    )

def new_message(message_or_event, needs_response, say, slack_client): 
    # queue message no matter what
    # TODO: santize text to remove the mark down
    queue_user_message(message_or_event['channel'], message_or_event['user'], message_or_event['text'])

    # either IM or got mentoned
    if needs_response:
        wait_msg = say(":hourglass_flowing_sand: 'Ol On!")
        resp = get_response(message_or_event['channel'])
        slack_client.chat_update(
            channel=message_or_event['channel'], 
            ts=wait_msg['ts'], 
            text = resp,
            blocks=[create_markdown_block(resp)]
        )

@app.event("app_home_opened")
def update_home_tab(client, event):
    client.views_publish(
        user_id = event['user'],
        view = {
            "type": "home",
            "blocks": get_home_page_blocks(event['user'])
        }
    )

# create a markdown text block after converting openai markdowns to slack markdowns
def create_markdown_block(text: str):
    conversions = {
        '**': '*',        # Bold
        '__': '_',        # Italic
        '~~': '~',        # Strikethrough
        '```': '```',     # Code block (same in Slack)
        '`': '`',         # Inline code (same in Slack)
        # Hyperlinks are left as they are because Slack automatically detects URLs and formats them.
    }
    
    # Replace based on the conversion dictionary
    # TODO do some fancy thing with the code blocks
    for md, slack_md in conversions.items():
        text = text.replace(md, slack_md)

    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": text
        }
    }

# home page block
def get_home_page_blocks(user_id):
    return [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"<@{user_id}> Wagwan mi bredah! How yu be?"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"I is *cocochat*. My deddy is Manolo (Danny) y Cabeza Huevo (Soumit). Yes, I has 2 deddys! Ma' deddys put _{config.get_llm_chat_model()}_ up my culito for your entertainment (its some ghetto ass shit be they is broke sooo .. :man-shrugging:). Poke around and I might even like it :eggplant:"
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
