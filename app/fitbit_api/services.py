import requests
from .secret import *

def dummy_api(url):

	# sending get request and saving the response as response object
	res = requests.get(url)

	# extracting data in json format
	data = res.json()
	print(data)
	return data

def profile_data_api(url, access_token):
	headers = {'Authorization': f'Bearer {access_token}'}
	res = requests.get(url, headers=headers)
	return res

def get_fresh_access_token(url,refresh_token):
	payload = {'grant_type': 'refresh_token', 'refresh_token': refresh_token}
	headers = {'Authorization' : f'Basic {client_secret_base64}', 'Content-Type' : 'application/x-www-form-urlencoded'}
	res = requests.post(url,headers=headers, data=payload)
	return res
