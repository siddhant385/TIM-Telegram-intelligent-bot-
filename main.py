import requests
import json
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import time
import random
import wikipedia

token = '2088282456:AAGoFCw13uWt2mXvp8rWXHrxgZTxAR5NSA8'
chat_id = ''
known_ids = []

def checkchat_id(chat_id):
	return len(known_ids) == 0 or str(chat_id) in known_ids

def send_safe_message(bot, chat_id, message):
	while(True):
		try:
			print('n','Message sent:\n{}'.format(bot.sendMessage(chat_id, message)),True)
			break
		except Exception as e:
			print(e)
def split_string(n, st):
	lst = ['']
	for i in str(st):
		l = len(lst) - 1
		if len(lst[l]) < n:
			lst[l] += i
		else:
			lst += [i]
	return lst
	
intro = '''
This bot is made by Siddhant Sharma 😎😎😎
If you like this bot please give star 🌟 to siddhant sharma github repsitory
Github repositry is 👉 https://github.com/siddhant385/bot
Enjoy 
'''
botintro = '''
Myself TIM
Tim Stands for Telegram Intelligent Manager
I was created as a hobby project by Master Siddhant
To know about my hobbys enter /hobbys
And ofcourse I can do many valuable works for you
and I have a twin sister which is more capable of me
	She can send emails 
	can download videos from youtube
	and many more
but she is greedy if you want her of $5 and for more info 
Send an email to techforyou385@gmail.com with subject TIM Mk2
'''
help = '''
/news : Tells the current news
/thoughts : Instantly get a motivational thoughts
/toss : perform a toss for you
/introduce_about_yourself : Know more about bot
/wikipedia <topic> : inplace of topic enter the name of object you want from wikipedia
/help : know about commands
'''
	
def toss():
	send_safe_message('toss command found')
	send_safe_message('performing toss via coing')
	send_safe_message('coin is in the air and the result is')
	time.sleep(5)
	a = random.choice(1,2)
	if a == 1:
		send_safe_message('Heads')
	elif a == 2:
		send_safe_message('Tails')

def handle(msg):
		chat_id = msg['chat']['id']
		message_id = msg['message_id']      
		command = msg['text']
		print('n','\n\t\tGot message from ' + str(chat_id) + ': ' + msg['text'] + '\n\n',True)

		if command == '/news':
			r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=1ca09761917e4bd29a086a9dd4832902')
			d = json.loads(r.content)
			send_safe_message(bot,chat_id,'**TODAYS NEWS HEADLINES ARE**')
			for i in range(10):
				articles = d['articles'][i]['title']
				newsdlk = articles
				print(newsdlk)
				bot.sendMessage(chat_id,newsdlk)
		elif command == '/thoughts':
			try:
				params ={
					'method':'getQuote',
					'lang':'en',
					'format':'json'
					}
				res = requests.get('http://api.forismatic.com/api/1.0/',params)
				jsonText =json.loads(res.text)
				quote = jsonText["quoteText"]
				bot.sendMessage(chat_id, quote)
			except Exception as something:
				response = ('sorry sir unable to get the quote maybe due to network problem or some error')
		elif command == '/toss':
			bot.sendMessage(chat_id,'toss command found')
			bot.sendMessage(chat_id,'performing toss via coin')
			bot.sendMessage(chat_id,'coin is in the air and the result is')
			list = [0,1]
			a = random.choice(list)
			if a == 1:
				bot.sendMessage(chat_id,'Heads')
			else:
				bot.sendMessage(chat_id,'Tails')
		
		elif command == '/start':
			bot.sendMessage(chat_id,intro)
		elif command.startswith('/wikipedia'):
			command = command.replace("/wikipedia", "")
			results = wikipedia.summary(command, sentences = 3)
			bot.sendMessage(chat_id,"According to Wikipedia")
			bot.sendMessage(chat_id,results)
		
		elif command == '/introduce_about_yourself' :
			bot.sendMessage(chat_id,botintro)

		elif command == '/help':
			bot.sendMessage(chat_id,help)
		else:
			bot.sendMessage(chat_id,'Sorry command not found please send commnads from below')
			bot.sendMessage(chat_id,help)



print('s','Setup done')
print('i','Starting')
bot = telepot.Bot(token)
bot.message_loop(handle)
if len(known_ids) > 0:
	helloWorld = 'I am ready'
	for known_id in known_ids: send_safe_message(bot, known_id, helloWorld)
	print(helloWorld)
send_safe_message(bot,chat_id,'hello started')
print('s','Started')
while 1:
	time.sleep(1)
