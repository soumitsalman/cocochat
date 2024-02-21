import datetime
import config
from icecream import ic
from slack_bolt import App
from slack_sdk.errors import SlackApiError
# import chatmanager as cm
import re
import requests

# set up the initial app
app = App(
    token=config.get_slack_bot_token(),
    signing_secret=config.get_slack_signing_secret()
)

@app.message()
def receive_message(message, say, client): 
    new_message(
        message_or_event = message,         
        say = say, 
        slack_client = client, 
        # in a DM the conversation or call out of the bot name is usually ping pong, so respond
        needs_response=_needs_response(message)
    )

@app.event("app_mention")
def receive_mention(event, say, client):
    new_message(
        message_or_event = event,        
        say=say, 
        slack_client=client,
        needs_response=True # always respond when mentioned
    )

@app.event("app_home_opened")
def update_home_tab(client, event):
    ic("updating home page")
    if event['tab'] == "home":
        client.views_publish(
            user_id = event['user'],
            view = {
                "type": "home",
                "blocks": get_home_page_blocks(client, event['user'])
            }
        )

@app.command("/whatsnew")
def receive_whatsnew(command, respond, ack):
    ack()
    ic("/whatsnew", command['user_name'], command['text'])
    items = get_new_items(command['user_name'], command['text'] )
    for disp_block in get_displayblocks(items):
        respond(blocks = disp_block)
    

@app.action(re.compile("(positive|negative)"))
def receive_content_action(ack, action, body):
    ack()
    action_id, content_id, username = ic(action['action_id'], action['value'], body['user']['username'])
    post_user_engagement(username, content_id, action_id)

def post_user_engagement(username, content_id, action_id):
    auth_header = { "X-API-Key": config.get_internal_auth_token() }
    content_id_split = content_id.split('@')
    body = [
        {
            "username": username,
            "usersource": "SLACK",
            "cid": content_id_split[0],
            "source": content_id_split[1],
            "action": action_id 
        }
    ]
    ic(requests.post(
        f"{config.get_media_store_url()}/engagements", 
        json=body, 
        headers=auth_header).status_code)

def get_new_items(user, kind):
    auth_header = { "X-API-Key": config.get_internal_auth_token() }

    params = {
        "username": user,
        "usersource": "SLACK"        
    }    
    if kind:
        params["kind"] = kind     
        
    resp = requests.get(
        f"{config.get_media_store_url()}/contents", 
        params = params, 
        headers=auth_header)
    
    if ic(resp.status_code) == requests.codes["ok"]:
        return resp.json()
    else:
        return []

def get_displayblocks(items):
    date_element = lambda data: {
        "type": "plain_text",
        "text": f":date: {datetime.datetime.fromtimestamp(data.get('created')).strftime('%b %d, %Y')}"
    }
    tags_element = lambda data: {
        "type": "plain_text",
        "text": f":card_index_dividers: {data.get('tags')[0]}"
    }
    subs_element = lambda data: {
        "type": "plain_text",
        "text": f":busts_in_silhouette: {data.get('subscribers', 0)}"
    }

    post_banner = lambda data: {
        "type": "context",
        "elements": [            
            {
                "type": "plain_text",
                "text": f":thumbsup: {data.get('likes', 0)}"
            },
            {
                "type": "plain_text",
                "text": f":left_speech_bubble: {data.get('comments', 0)}"
            },   
            subs_element(data),                            
            tags_element(data),
            date_element(data)
        ]
    }
    channel_banner = lambda data: {
        "type": "context",
        "elements": [
            subs_element(data),                            
            tags_element(data)
        ]
    }
    body = lambda data: {        
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": f"[<{data.get('url')}|{data.get('channel')}>] *{data.get('title', '')}*\n{data.get('excerpt')}"
		}
    }
    value = lambda data: f"{data.get('cid')}@{data.get('source')}"
    
    action = lambda data: {    
		"type": "actions",
		"elements": [
			{
                "action_id": f"positive",
                "type": "button",
				"text": {
					"type": "plain_text",
					"text": ":ok_hand:",
                    "emoji": True
				},
				"value": value(data)
			},
			{
                "action_id": f"negative",
                "type": "button",
				"text": {
					"type": "plain_text",
					"text": ":shit:",
                    "emoji": True
				},
				"value": value(data)
			}
		]
	}
    
    for item in items:
        if item["kind"] == "channel":
            new_set = [
                channel_banner(item),
                body(item),
                action(item)
            ]
        else:
            new_set = [
                post_banner(item),
                body(item),
                action(item)
            ]
        yield new_set
    
    

def new_message(message_or_event, say, slack_client, needs_response):  
    say ("I actually don't do anything. I just sit here and look pretty")
    # queue message no matter what    
    # cm.add_user_message(
    #     message_or_event['channel'], 
    #     get_user_data(message_or_event['user'], slack_client)['name'], 
    #     _sanitize_message_text(message_or_event['text'], slack_client))

    # # either IM or got mentoned
    # if needs_response:
    #     # wait_msg = say(":hourglass_flowing_sand: 'Ol On!")
    #     slack_client.reactions_add(
    #         channel = message_or_event["channel"],
    #         timestamp = message_or_event["ts"],
    #         name = "hourglass_flowing_sand"
    #     )
    #     resp = cm.get_bot_response(message_or_event['channel'])
    #     say(
    #         text = resp,
    #         blocks=[_create_markdown_block(resp)]
    #     )

def _needs_response(message_or_event):
    return ((message_or_event['channel_type'] == "im") or config.get_chat_bot_name() in message_or_event['text'])

def _sanitize_message_text(text: str, slack_client):
    # this is a function within a function because the signature of extract_ids function is allowed to take only 1 parameter as required by re.sub
    # this way i can use the slack_event value
	def extract_ids(match):
		matched_text = match.group(0)        
		if matched_text.startswith("<@") and matched_text.endswith(">"):
			user_id = matched_text[2:-1]
			return get_user_data(user_id, slack_client)['name']
		elif matched_text.startswith('<#') and matched_text.endswith('>'):
			channel_id, channel_name = matched_text[2:-1].split('|')
            # if there is no channel name in the expression it means its a private channel
			return f"#{(channel_name if channel_name != '' else get_channel_data(channel_id, slack_client)['name'])} channel"
	
	return re.sub(r'<@[\w]+>|<#[\w]+\|[\w]*>', extract_ids, text)

# create a markdown text block after converting openai markdowns to slack markdowns
def _create_markdown_block(text: str):
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
def get_home_page_blocks(slack_client, user_id):
    # name = get_user_data(user_id=user_id, slack_client=slack_client)['name']
    # cm.add_user_message(channel=cm.CHAT_MANAGER_CHANNEL, user = None, message = f"{name} wants to know who you are. Greet them as @{name} and tell him all about yourself. Make your responses sound like snoop dogg.")
    # resp = cm.get_bot_response(channel=cm.CHAT_MANAGER_CHANNEL)
    # return config.get_home_page_content(resp)
    return [		
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": """/whatsnew <param-kind> <param-count> will give you all the new posts or channels that might be interesting to you. 
<param-kind> can be either post or channel. <param-count> can be an int"""
            }
        }
    ]

# team/workspace data
_users = {}
_channels = {}
_UNKNOWN_USER = "user"
_INACCESSIBLE_CHANNEL = "INACCESSIBLE CHANNEL"
# structure is expected to be
# _users = {
#     "<user_id_value>": {
#         "name": "<name_value>",
#         "long_name": "<long_name_value>"
# 	}
# }

# _channels = {
#     "<channel_id_value>": {
#         "name": "<name_value>",
#         "is_im": True/False,
# 	}
# }

def get_user_data(user_id, slack_client):
    # user_id = message_or_event['user']
    if user_id not in _users:           
        try:
            user_data = slack_client.users_info(user = user_id)['user']
            _users[user_id] = {
				"name": user_data['name'],
				"long_name": user_data['real_name']
			}
        except SlackApiError: # user is in accessible
            _users[user_id] = {
				"name": _UNKNOWN_USER,
				"long_name": _UNKNOWN_USER
			}
            
    return _users[user_id]

def get_channel_data(channel_id, slack_client):
    if channel_id not in _channels: # cache data
        try:
            channel_data = slack_client.conversations_info(channel = channel_id)['channel']
            _channels[channel_id] = {
				# for channels use the channel name and for DMs this will be None
				"name": channel_data.get("name"),
				"is_im": channel_data['is_im']
			}
        except SlackApiError: # slack channel is inaccessible
            _channels[channel_id] = {
				"name": _INACCESSIBLE_CHANNEL,
				"is_im": False
			}             
        
    return _channels[channel_id]
 
