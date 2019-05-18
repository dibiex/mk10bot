from combo import * 
import random
hp1 = 100
hp2 = 100

headers = {'charset': 'utf-8'}

url1 ="http://10.81.176.97/get_status"
data1={
  "key": "wyccugxu9h995u7n"
}
array = ["up","down","left","right","front_punch","back_punch","front_kick","back_kick","interact","throw","block"]

response = requests.post(url1, json=data1, headers=headers)
print(response.json())
player_number = response.json()["player"]

def three_moves():

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

def two_moves():
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

def Rand():
    number = random.randint(1, 5)
    if(number == 1):
        three_moves()
    if(number == 2):
        two_moves()
        #block
    if(number == 3):
        JJL()
    if(number == 4):
        COMBO2()
    if(number == 5):
        ALI()

def Rand2():
    number = random.randint(1, 5)
    if(number == 1):
        ADJ()
        COMBO3()
    if(number == 2):
        JJL()
        time.sleep(0.6)
        block()
    if(number == 3):
        DLI()
    if(number == 4):
        three_moves()
        DLI()
    if(number == 5):
        two_moves()



def Rand3():
    number = random.randint(1, 5)
    if(number == 1):
        ADJ()
        COMBO3()
    if(number == 2):
        three_moves()
        ALI()
    if(number == 3):
        two_moves()
    if(number == 4):
        SDK()
        COMBO2()    
    if(number == 5):
        SDK()
        COMBO3()

def Rand4():
    number = random.randint(1, 4)
    if(number == 1):
        DAJ()
        COMBO3()
    if(number == 2):
        three_moves()
        DLI()
    if(number == 3):
        COMBO4()    
    if(number == 4):
        SAK()
        COMBO3()

def Main(data):
#player_number = response.json ceva
    print('intru')
    healthOld = 3

    
    if(player_number == "p1"):
        myposx = data[0]
        myposy = data[1]
        enemyposx = data[2]
        enemyposy =  data[3]
        health = data[4]
        damage1 = data[6]
        damage2 = data[7]
    else:
        myposx = data[2]
        myposy = data[3]
        enemyposx = data[0]
        enemyposy = data[1]
        health = data[5]
        damage1 = data[7]
        damage2 = data[6]

    # if damage > 0.1 and damage < 0.3
        #blcked

    p1dir = 0
    p2dir = 1

    if(myposx < 300):
        p1dir = 0
        p2dir = 1
    else:
        if myposx > 500:
            p1dir = 1
            p2dir = 0
        else:
            if myposx - enemyposx < 0:
                p1dir = 0
                p2dir = 1
            else:
                p1dir = 1
                p2dir = 0

    print(health+"\n\n\n\n\n"+health)
    if(health >= 2.8):
        if(player_number == "p1" ):
            SAK()
            SDK()
            SAK()
            SDK()
            SAK()
            SDK()
        else:
            SDK()
            SAK()
            SDK()
            SAK()
            SDK()
            SAK()
            
    
    distance = float(myposx) - float(enemyposx)

    if abs(distance) < 60:
        #close
        print("They're close")
        number = random.randint(1, 13)
        if(number == 1 or number == 13):
            JJL()
        if(number == 2):
            COMBO2()
        if(number == 3 or number ==11):
            COMBO3()
        if(number == 4 or number == 12):
            SDK()
            block()
        if(number == 5 or number == 6 or number == 7):
            ALI()
        if(number == 8 or numer == 9 or number == 10):
            DLI()
            
        if distance > 0:
            #im right
            Rand()
        else:
            #im left
            Rand2()
    else:
        if (p1dir == 1):
        #im far right
            Rand3()

        if (p1dir == 0):
        #im far left 
            Rand4()

    if (damage1 > 0.15):
        #I was hit
        #print("DAMAGE\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        block()
        J()
        return
    else:
        if (damage2 > 0.1):
            # print("Sdk\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            SAK()
            SDK()
            SAK()
            SDK()
            SAK()
            SDK()
            


    if(myposx == "null" or enemyposx == "null"):
        SDK()
        SAK()
        block()


    print('ies')


if __name__ == "__main__":
    while True:
        try:
            Main()
        except:
            print("fff")