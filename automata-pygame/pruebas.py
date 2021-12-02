from typing import BinaryIO


def manualrules(x):
    if x>255:
        x=255 
    elif x<0:
        x=0   
    y=format(x,"b")
    print(str(y))
    rules=[0,0,0,0,0,0,0,0]
    for i in range(len(y)) :
        rules[-(int(i)+1)]=int(y[-(int(i)+1)])   
    return rules


print(manualrules(98))