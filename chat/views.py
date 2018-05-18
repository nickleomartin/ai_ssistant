import requests
import random 

from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
	context = {}
	return render(request,'chat/index.html',context)


def chatbot(request):

	## Make api call
	text = request.GET.get('q','')
	print(text)
	rasa_response = requests.get("http://localhost:5000/parse",params={"q":text})
	# response = response.json()
	print(rasa_response.json())

	## Handle reponse 
	bot_response = bot_response_logic(rasa_response.json())
	print(bot_response)
	
	context = {'response': bot_response}
	return JsonResponse(context)




COULD_NOT_PARSE_MSGS = [
	"Sorry, I don't know it",
	"Next time I will know, but not now",
	"Sorry, can't get what do you mean",
	"Try something else"
]

GREET_MSGS = ["Hola!", "Privet!", "Xin chào!"]
SEARCH_MSGS = ['I have found something!', 'I am looking....found one!']
AFFIRM_MSGS = ['Affirming it!', 'Affirming one!']
GOODBYE_MSGS = ['cheers!','goodbye!','ciao muchacho']


INTENT_GREET = "greet"
INTENT_SEARCH = "restaurant_search"
INTENT_AFFIRM = "affirm"
INTENT_GOODBYE = "goodbye"

def bot_response_logic(api_response):
	if not "intent" in api_response or api_response["intent"] is None:
		# later we can do something with unparsed messages, probably train bot
		# self.unparsed_messages.append(msg)
		return random.choice(COULD_NOT_PARSE_MSGS)

	if api_response["intent"]["name"] == INTENT_GREET:
		return random.choice(GREET_MSGS)

	if api_response["intent"]["name"] == INTENT_SEARCH:
		return random.choice(SEARCH_MSGS)

	if api_response["intent"]["name"] == INTENT_AFFIRM:
		return random.choice(AFFIRM_MSGS)

	if api_response["intent"]["name"] == INTENT_GOODBYE:
		return random.choice(GOODBYE_MSGS)

	# same approach for all questions
	# if api_response["intent"]["name"] in INTENTS_QUESTION and len(api_response["entities"]) > 0:
	# 	for e in api_response["entities"]:
	# 		if e["entity"] == ENTITY_QUERY:
	# 			return self.get_short_answer(e["value"])

	# self.unparsed_messages.append(msg)
	return random.choice(COULD_NOT_PARSE_MSGS)