import requests

def dummy_api(url):
  
	# sending get request and saving the response as response object 
	res = requests.get(url) 
	  
	# extracting data in json format 
	data = res.json() 
	print(data)
	return data