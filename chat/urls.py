from django.urls import path
from . import views

urlpatterns = [
				path("index",views.index),
				path("chatbot",views.chatbot),
				]