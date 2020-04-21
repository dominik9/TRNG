
import json
from numpy import double

import reverseFloatNum
#wartosci początkowe

#S1 = 0.1, T1 = 0.2, S2 = 0.3, T2 = 0.4, S3 = 0.5, T3 = 0.6.
S1 = double(0.1)
T1 = double(0.2)
S2 = double(0.3)
T2 = double(0.4)
S3 = double(0.5)
T3 = double(0.6)

def fun_G(a,x0):
    if x0 <= a:
        return x0/a
    else:
        return (1-x0)/(1-a)

def tentMap(si,ti,mi):
    rew_m = reverseFloatNum.reverseFloat(mi)
    g_i = fun_G((si+mi)%1,(ti+rew_m)%1)
    ti_1 = (g_i+si)%1
    si_1 = fun_G(min((g_i+rew_m)%1,ti),max((g_i+rew_m)%1,ti))
    return [si_1,ti_1]

def mulList(a,mulList):
    for m in range(len(mulList)):
        mulList[m] = mulList[m] * a
    return mulList

def addLists(a,b):
    a[0] = a[0] + b[0]
    a[1] = a[1] + b[1]
    return a


def getOneRandomPostProcesingSTvaribles(real_128_move):
    x1 = (S1,T1)
    x2 = (S2,T2)
    x3 = (S3,T3)
    for counter_M in range(len(real_128_move)):
        new_x1 = tentMap(x1[0],x1[1],real_128_move[counter_M])
        new_x2 = tentMap(x2[0],x2[1],real_128_move[counter_M])
        new_x3 = tentMap(x3[0],x3[1],real_128_move[counter_M])
        x1_1 = addLists(mulList(0.95,new_x1), mulList(0.025,addLists(new_x2,new_x3)))
        #print(x1_1)
        x2_1 = addLists(mulList(0.95,new_x2), mulList(0.025,addLists(new_x3,new_x1)))
        x3_1 = addLists(mulList(0.95,new_x2), mulList(0.025,addLists(new_x1, new_x2)))
        x1 = x1_1
        x2 = x2_1
        x3 = x3_1
    return [x1,x2,x3]

def startConversionto256bit():
    with open('real_num.json','r') as file:
        data = json.load(file)
        real128 = []
        nums_not_konwerted_to_bin = []
        for i in range(len(data)):
            real128.append(double(data[i]))
            if len(real128) == 128:
                nums_not_konwerted_to_bin.append(getOneRandomPostProcesingSTvaribles(real128))
                real128 = []


        return nums_not_konwerted_to_bin

with open('step3.json','w') as file:
    json.dump(startConversionto256bit(), file)

