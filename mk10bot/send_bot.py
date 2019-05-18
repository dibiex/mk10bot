from combo import * 
import random
hp1 = 100
hp2 = 100

headers = {'charset': 'utf-8'}

url1 ="http://10.81.176.53/get_status"
data1={
  "key": "wyccugxu9h995u7n"
}
#array = ["up","down","left","right","front_punch","back_punch","front_kick","back_kick","interact","throw","block"]

response = requests.post(url1, json=data1, headers=headers)
player_number = response.json()['player']

def Rand():
    number = random.randint(1, 4)
    if(number == 1):
        three_moves()
    if(number == 2):
        two_moves()
        #block
    if(number == 3):
        JJL()
    if(number == 4):
        COMBO2()

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
    if(number == 5):
        two_moves()



def Rand3():
    number = random.randint(1, 7)
    if(number == 1):
        ADJ()
        COMBO3()
    if(number == 2):
        JJL()
        time.sleep(0.6)
        block()
    if(number == 3):
        ALI()
    if(number == 4):
        three_moves()
    if(number == 5):
        two_moves()
    if(number == 6):
        SDK()
        COMBO2()    
    if(number == 7):
        SDK()
        COMBO3()

def Rand4():
    number = random.randint(1, 7)
    if(number == 1):
        DAJ()
        COMBO3()
    if(number == 2):
        JJL()
        time.sleep(0.6)
        block()
    if(number == 3):
        ALI()
    if(number == 4):
        three_moves()
    if(number == 5):
        two_moves()
    if(number == 6):
        COMBO4()    
    if(number == 7):
        SAK()
        COMBO3()

def Main(data):
#player_number = response.json ceva
    healthOld = 3
    while(True):


        print(data)
        
        if(player_number == "p1"):
            myposx = data[0]
            myposy = data[1]
            enemyposx = data[2]
            enemyposy =  data[3]
            health = data[4]
        else:
            myposx = data[2]
            myposy = data[3]
            enemyposx = data[0]
            enemyposy = data[1]
            health = data[5]

        if (float(healthOld) - float(health) > 0.2):
            #I was hit
            block()
            J()

        if(myposx == "null" or enemyposx == "null"):
            SDK()
            SAK()
            block()
            continue

        distance = float(myposx) - float(enemyposx)

        if abs(distance) < 70:
            #close
            number = random.randint(1, 4)
            if(number == 1):
                JJL()
            if(number == 2):
                COMBO2()
            if(number == 3):
                COMBO3()
            if(number == 4):
                SDK()
                block()
            if distance > 0:
                #im right
                Rand()
            else:
                #im left
                Rand2()
        else:
            if (distance > 0):
            #im far right
                Rand3()
            if (distance < 0):
            #im far left 
                Rand4()



if __name__ == "__main__":
    while True:
        try:
            Main()
        except:
            print("fff")