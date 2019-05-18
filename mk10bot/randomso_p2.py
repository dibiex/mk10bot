import requests
import response
import time
import random
from combos import SDK, SAK, SAL , ADJ, DAJ

url = "http://10.81.176.53/command"
key = "9b8xwejf6iltaij8"

headers = {'charset': 'utf-8'}
array = ["up","down","left","right","front_punch","back_punch","front_kick","back_kick","interact","throw","block"]

def three_set_move():

    move1= random.choice(array);
    data = {"key": key, "commands": {move1: True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    move2= random.choice(array);
    data = {"key": key, "commands": {move2: True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
    move3= random.choice(array);
    data =  {"key": key, "commands": {move3: True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {move1: False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {move2: False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
    data =  {"key": key, "commands": {move3: False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

def two_set_move():
    move1= random.choice(array);
    data = {"key": key, "commands": {move1: True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    move2= random.choice(array);
    data = {"key": key, "commands": {move2: True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
    data = {"key": key, "commands": {move1: False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {move2: False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
def one_set_move():

    move1= random.choice(array);
    data = {"key": key, "commands": {move1: True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
    data = {"key": key, "commands": {move1: False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

if __name__ == "__main__":
    while True:

        number = random.randint(1, 8)
        if(number == 1):
            one_set_move()
        if(number == 2):
            two_set_move()
        if(number == 3):
            three_set_move()
        if(number == 4):
            SDK()
        if(number == 5):
            SAL()
        if(number ==6 ):
            ADJ()
        if(number == 7):
            DAJ()
        if(number == 8):
            SAK()            
