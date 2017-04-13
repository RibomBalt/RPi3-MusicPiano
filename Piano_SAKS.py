from sakshat import SAKSHAT
# from sakspins import SAKSPins as PINS
# import time

#Declare the SAKS Board
SAKS = SAKSHAT()
soundToNum = {'C':1,'D':2,'E':3,'F':4,'G':5,'A':6,'B':7,'+':0}
temp = None
def ledOn(string):
    #1-7显示音调，0显示升调
    global temp
    if string[-1] == '+':
        temp = soundToNum[string[-2]]
        SAKS.ledrow.on_for_index(0)
        SAKS.ledrow.on_for_index(temp)
    else:
        temp = soundToNum[string[-1]]
        SAKS.ledrow.on_for_index(temp)

def ledOff(string):
    while temp != None:
        SAKS.ledrow.off_for_index(0)
        SAKS.ledrow.off_for_index(temp)

def digitalPlay(string):
    if len(string) == 3:
        strToDisplay = string[0]+'#'+'.'+str(soundToNum[string[1]])+'.'+'#'
    else:
        strToDisplay = string[0]+'#'+str(soundToNum[string[1]])+'#'
    SAKS.digital_display.show(strToDisplay)

def cleanUp():
    SAKS.ledrow.off()
    SAKS.digital_display.show('####')
