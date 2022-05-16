from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=4, trigger=27)
while True:
    print(ultrasonic.distance*100)