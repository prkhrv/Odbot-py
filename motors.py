import RPi.GPIO as gpio
import time

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)

def move_forward(sec):
 init()
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()

def move_reverse(sec):
 init()
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 gpio.cleanup()

def stop(sec):
 init()
 gpio.output(17, False)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()
 
def move_right(sec):
 init()
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()
 
def move_left(sec):
 init()
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 gpio.cleanup()


#print("forward")
#forward(2)
#print("stop")
#stop(1)
#print("left")
#left(1)
#print("reverse")
#reverse(1)