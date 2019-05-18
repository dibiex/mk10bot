import requests
import urllib3
import response

headers = {'charset': 'utf-8'}

url1 ="http://10.81.176.97/admin"
data1={
  "key": "gx0bni64t6s99dhp",
  "type": "change_teams",
  "team1": "T15",
  "team2": "T15_P2"
}
print(data1)

response = requests.post(url1, json=data1, headers=headers)
print(response.status_code)
print(response.json())


url = "http://10.81.176.97/stream_config"
data = {"key": "wyccugxu9h995u7n","ip": "10.81.149.9","port": 5005,"downscale_ratio": 0.6}
print(data)
response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
