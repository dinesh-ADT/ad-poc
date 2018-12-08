from django.http import HttpResponse
from . import services
import json


def index(request):

	# api-endpoint 
	url = 'https://reqres.in/api/users?page=2'
	data = services.dummy_api(url)
	return HttpResponse(json.dumps(data))