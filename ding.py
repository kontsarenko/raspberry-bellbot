import RPi.GPIO as GPIO
import time

def bing():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(7,GPIO.OUT)
  print "LED on"
  GPIO.output(7,GPIO.HIGH)
  time.sleep(1)
  print "LED off"
  GPIO.output(7,GPIO.LOW)

if __name__ == '__main__':
    bing()
