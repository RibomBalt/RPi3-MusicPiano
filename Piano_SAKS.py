from sakshat import SAKSHAT
from sakspins import SAKSPins as PINS
import time

#Declare the SAKS Board
SAKS = SAKSHAT()
def ledOper(string):
	#1-7显示音调，8显示升调
	ledNum = {'C':1,'D':2,'E':3,'F':4,'G':5,'A':6,'B':7,'+':8}
	numOfLed = ledNum[string[-1]]
	if numOfLed == 8:
		sound = ledNum[string[-2]]
		SAKS.ledrow.items[8].on()
		SAKS.ledrow.items[sound].on()
		time.sleep(0.5)
		SAKS.ledrow.items[8].off()
		SAKS.ledrow.items[sound].off()
	else:
		SAKS.ledrow.items[numOfLed].on()
		time.sleep(0.5)
		SAKS.ledrow.items[numOfLed].off()
		#可以实现输入下一个音符时灭灯，而不是固定时间，不过我觉得
		#如果每个音时间固定就没什么必要
