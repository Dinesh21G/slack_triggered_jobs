import slackmy_clientent, time

token = <YOUR BOT AUTH TOKEN>

my_client = slackmy_clientent.Slackmy_clientent(token)
assert my_client.rtm_connect()

jobs = []

HI_TEXT='''Hi there!

Please Type help,  (or) we will play hi - hi game
'''

HELP_TEXT ='''These are the commands I recognise
'''
for job in jobs:
	HELP_TEXT += '\n'+job

def get_valid_msg():
'''
Wait till a valid message is received.
'''
	while True:
		messages = my_client.rtm_read()
		for message in messages:
			if ('bot_id' not in message and 'channel' in message and 'text' in message and 'type' in message):
				channel = message['channel']
				msg = message['text']
				print('Received  : {0}'.format(msg))
				return channel, msg
	time.sleep(3)
	return None

def do_myjob(channel, job):
'''
Do integrate with your working model, Use any async mode to run jobs.
And obviously, send the result back.
'''
	pass

def collect_data(channel, msg):
'''
Its always good to hear people who showed interest at us.
And to let know, if something related is actively in progress.
'''
	pass

while True:
	channel, msg = get_valid_msg()
	if msg.lower() in ['hi', 'hey', 'hello']:
		my_client.api_call('chat.postMessage', channel=channel, text=HI_TEXT, as_user='true')
	elif msg.lower() == "help":
		my_client.api_call('chat.postMessage', channel=channel, text=HELP_TEXT, as_user='true')
	elif msg in jobs:
		do_myjob(channel, msg)
		my_client.api_call('chat.postMessage', channel=channel, text="your job has been posted", as_user='true')
	else:
		collect_data(channel, msg)
		my_client.api_call('chat.postMessage', channel=channel, text="Uh-huh..  Interesting... I ll let it know to my team", as_user='true')
