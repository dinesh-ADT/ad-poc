import requests

def dummy_api(url):
  
	# sending get request and saving the response as response object 
	res = requests.get(url) 
	  
	# extracting data in json format 
	data = res.json() 
	print(data)
	return data

def profile_data_api(access_token,fitbit_id,url):
	headers = {'Authorization': f'Bearer {access_token}'}
	r = requests.get(url, headers=headers)
	return r.json()
