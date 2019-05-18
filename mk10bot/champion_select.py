import requests
import urllib3
import response

headers = {'charset': 'utf-8'}

url1 ="http://10.81.176.97/player_select"
data1={
	"key" : "wyccugxu9h995u7n",
	"champion" : "scorpio"	
}
print(data1)
response = requests.post(url1, json=data1, headers=headers)
print(response.json())
