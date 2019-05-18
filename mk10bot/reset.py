import requests
import response

url = "http://10.81.176.53/admin"
key = "gx0bni64t6s99dhp"
headers = {'charset': 'utf-8'}
data={"key": key, "type" : "reset_game_after_endscreen", "hide_post_game_details": True}
response = requests.post(url, json=data, headers=headers)
print(response.json())