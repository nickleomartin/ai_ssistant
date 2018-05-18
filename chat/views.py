import requests

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	# text = "I am looking for a mexican resturant in my area"
	# q = request.GET.get('q','')
	# print(q)
	# response = requests.get("http://localhost:5000/parse",params={"q":q})
	# # response = response.json()
	# return HttpResponse(response)
	context = {'random':'7538724532'}
	return render(request,'chat/index.html',context)