from django.http import HttpResponse
from . import services
import json
from .models import Member, UserToken


def index(request):

	# api-endpoint
	url = 'https://reqres.in/api/users?page=2'
	data = services.dummy_api(url)
	return HttpResponse(json.dumps(data))

def profile_data(request,user):

	member = Member.objects.get(name=user)
	user_token = UserToken.objects.get(member=member)
	access_token = user_token.access_token
	fitbit_id = user_token.device_id
	profile_url = f'https://api.fitbit.com/1/user/{fitbit_id}/profile.json'
	res = services.profile_data_api(profile_url, access_token)
	data = res.json()


	if res.status_code == 401 and data['errors'][0]['errorType'] == "expired_token":
		# print(data['errors'][0]['errorType'],res.status_code)
		refresh_token = user_token.refresh_token
		url = 'https://api.fitbit.com/oauth2/token'
		# print("refresh token",refresh_token)
		token_res = services.get_fresh_access_token(url,refresh_token)
		token_data = token_res.json()
		# print('token_data',token_data)
		user_token.access_token = token_data['access_token']
		user_token.refresh_token = token_data['refresh_token']
		user_token.save()
		res = services.profile_data_api(profile_url,token_data['access_token'])

	return HttpResponse(res)
