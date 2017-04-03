import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
print('testing')
GPIO.setwarnings(False)
GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)
