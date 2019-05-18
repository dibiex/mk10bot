import requests
import response
import time

url = "http://10.81.176.53/command"
key = "wyccugxu9h995u7n"
headers = {'charset': 'utf-8'}
def SAL():
    data = {"key": key, "commands": {"down": True}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)

    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"back_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data =  {"key": key, "commands": {"down": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)


    data = {"key": key, "commands": {"back_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)


def ADJ():

    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
    data = {"key": key, "commands": {"front_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)

    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"front_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

def SAK():
    data = {"key": key, "commands": {"down": True}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)

    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"front_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"down": False}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)

    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"front_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

def SDK():
    data = {"key": key, "commands": {"down": True}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)

    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"front_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"down": False}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)

    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"front_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

def DAJ():
    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

if __name__ == "__main__":
    # SAL()
    # time.sleep(1.3)
    # ADJ()
    # time.sleep(2.1)
    # data = {"key": key, "commands": {"throw": True}}
    # response = requests.post(url, json=data, headers=headers)
    # time.sleep(.02)
    # data = {"key": key, "commands": {"throw": False}}
    # response = requests.post(url, json=data, headers=headers)
    # time.sleep(3)
    while True:
        SDK()
        time.sleep(0.5)
        SAK()
        time.sleep(0.5)
    # ADJ()