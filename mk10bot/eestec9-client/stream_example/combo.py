import requests
import responses
import time

url = "http://10.81.176.97/command"
key = "wyccugxu9h995u7n"
headers = {'charset': 'utf-8'}
# def SAL():
#     data = {"key": key, "commands": {"down": True}}
#     response = requests.post(url, json=data, headers=headers)

#     time.sleep(.02)

#     data = {"key": key, "commands": {"left": True}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)

#     data = {"key": key, "commands": {"back_kick": True}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)

#     data =  {"key": key, "commands": {"down": False}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)

#     data = {"key": key, "commands": {"left": False}}
#     response = requests.post(url, json=data, headers=headers)

#     time.sleep(.02)


#     data = {"key": key, "commands": {"back_kick": False}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)


def ADJ():

    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)

    time.sleep(.02)

    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)


    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    
    data = {"key": key, "commands": {"front_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    



    data = {"key": key, "commands": {"front_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(1.9)

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
    time.sleep(0.5)

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
    time.sleep(0.5)



def DAJ():
    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)


    data = {"key": key, "commands": {"front_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(1.9)


def AI():
    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(0.6)

def DI():
    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(0.6)

def DL():
    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)   
    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)  
    time.sleep(0.8)
 

def AL():
    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)   
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)  
    time.sleep(0.8)
 

def SI():
    data = {"key": key, "commands": {"down": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"down": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(0.8)

def JJL():
    data = {"key": key, "commands": {"front_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(0.95)

def J():
    data = {"key": key, "commands": {"front_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(0.3)

def K():
    data = {"key": key, "commands": {"front_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(0.5)
def A():
    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
def D():
    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

def I():
    data = {"key": key, "commands": {"back_punch": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_punch": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    time.sleep(0.6)    

def AK():
    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"front_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
#def SDL():
#     data = {"key": key, "commands": {"down": True}}
#     response = requests.post(url, json=data, headers=headers)

#     time.sleep(.02)

#     data = {"key": key, "commands": {"right": True}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)

#     data = {"key": key, "commands": {"back_kick": True}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)

#     data =  {"key": key, "commands": {"down": False}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)

#     data = {"key": key, "commands": {"right": False}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)


#     data = {"key": key, "commands": {"back_kick": False}}
#     response = requests.post(url, json=data, headers=headers)
#     time.sleep(.02)

# def SAJ():

def COMBO1A():
    K()
    SAK()
    JJL()

def COMBO1B():
    K()
    SDK()
    JJL()
def COMBO2():
	JJL()
	time.sleep(0.5)
	SAK()
	AK()
	# time.sleep(0.5)
	DAJ()
	JJL()


def COMBO3():
	JJL()
	time.sleep(0.5)
	SAK()
	AK()
	# time.sleep(0.5)
	DAJ()
	JJL()
	time.sleep(0.5)
	SDK()
	JJL()


def COMBO4():
	SAK()
	JJL()
	time.sleep(0.5)
	SDK()
	JJL()
	time.sleep(0.5)
	SAK()
	JJL()
def COMBOSDK():
    SAK()
    SDK()
    SAK()
    SDK()
    SAK()

def DLI():
    data = {"key": key, "commands": {"right": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)   
    data = {"key": key, "commands": {"right": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    I()

def ALI():
    data = {"key": key, "commands": {"left": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)   
    data = {"key": key, "commands": {"left": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"back_kick": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    I()
def U():
    data = {"key": key, "commands": {"throw": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)
    data = {"key": key, "commands": {"throw": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)

def block():

    data = {"key": key, "commands": {"block": True}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(1)
    data = {"key": key, "commands": {"block": False}}
    response = requests.post(url, json=data, headers=headers)
    time.sleep(.02)


if __name__ == "__main__":
    while True:
        SAL()
        time.sleep(1.3)
        ADJ()
        # time.sleep(2.1)
        # data = {"key": key, "commands": {"left": True}}
        # response = requests.post(url, json=data, headers=headers)
        # time.sleep(.02)
        # data = {"key": key, "commands": {"left": False}}
        # response = requests.post(url, json=data, headers=headers)
        # time.sleep(.02)
        # data = {"key": key, "commands": {"throw": False}}
        # response = requests.post(url, json=data, headers=headers)
        SAK()
        DI()
        DI()
        DI()
        DI()
        # # i=0
        # # while (i<8):
        # # 	AI()
        # # 	time.sleep(0.23)
        # # 	i=i+1
        SDK()
        time.sleep(0.5)
        ADJ()

        # data = {"key": key, "commands": {"block": True}}
        # response = requests.post(url, json=data, headers=headers)
        # time.sleep(.02)
        # data = {"key": key, "commands": {"flip_stance": True}}
        # response = requests.post(url, json=data, headers=headers)
        # time.sleep(.02)
        # data = {"key": key, "commands": {"block": False}}
        # response = requests.post(url, json=data, headers=headers)
        # time.sleep(.02)
        # data = {"key": key, "commands": {"flip_stance": False}}
        # response = requests.post(url, json=data, headers=headers)
        # time.sleep(.02)SAK()
        
        D()
        D()
        A()
        DL()
        SDK()
        U()
        DL()
        SAK()
        COMBO3()
        # while True:
        #     SAK()
        #     SDK()
