from django.http import HttpResponse
from . import services
import json
from .users import *


def index(request):

	# api-endpoint
	url = 'https://reqres.in/api/users?page=2'
	data = services.dummy_api(url)
	return HttpResponse(json.dumps(data))

def profile_data(request,user):
	# print(user_data[user]['access_token'])
	access_token = user_data[user]['access_token']
	fitbit_id = user_data[user]['fitbit_id']
	url = f'https://api.fitbit.com/1/user/{fitbit_id}/profile.json'
	data = services.profile_data_api(access_token,fitbit_id,url)
	return HttpResponse(json.dumps(data))

