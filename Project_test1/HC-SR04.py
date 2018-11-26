from machine import Pin
import time
import machine

print("Program Start")
class Ultrasonic:
    def __init__(self, tPin, ePin):

        self.triggerPin = Pin("G30", mode=Pin.OUT, pull=None, alt=-1)
        self.echoPin = Pin("G31", mode=Pin.IN, pull=None, alt=-1)

        # Init trigger pin (out)
        self.trigger = machine.Pin(self.triggerPin)
        self.trigger.init(machine.Pin.OUT)
        self.trigger.value(False)

        # Init echo pin (in)
        self.echo = machine.Pin(self.echoPin)
        self.echo.init(machine.Pin.IN)

    def distance_in_inches(self):
        return (self.distance_in_cm() * 0.3937)

    def distance_in_cm(self):
        start = 0
        end = 0

        # Create a microseconds counter.
        micros = Timer.Chrono()
        micros.reset()

        # Send a 10us pulse.
        self.trigger.value(True)
        Timer.sleep_us(10)
        self.trigger.value(False)

        # Wait 'till whe pulse starts.
        while(self.echo.value() == 0):
            start = micros.read_us()

        # Wait 'till the pulse is gone.
        while(self.echo.value() == 1):
            end = micros.read_us()

        # Deinit the microseconds counter
        micros.stop()

        # Calc the duration of the recieved pulse, divide the result by
        # 2 (round-trip) and divide it by 29 (the speed of sound is
        # 340 m/s and that is 29 us/cm).
        dist_in_cm = ((end - start) / 2) / 29

        return dist_in_cm

# setting pins to accomodate Ultrasonic Sensor (HC-SR04)
sensor1_trigPin = Pin("G30", mode=Pin.OUT)
sensor1_echoPin = Pin("G31", mode=Pin.IN)
sensor2_trigPin = Pin("G30", mode=Pin.OUT)
sensor2_echoPin = Pin("G31", mode=Pin.IN)

print("recive Input")
# sensor needs 5V and ground to be connected to pyboard's ground

# creating two Ultrasonic Objects using the above pin config

sensor1 = Ultrasonic(sensor1_trigPin, sensor1_echoPin)
sensor2 = Ultrasonic(sensor2_trigPin, sensor2_echoPin)

print("collect data")
print(sensor1)
print(sensor2)
print("done")
# using USR switch to print the sensor's values when pressed

#switch = pyb.Switch()

# function that prints each sensor's distance
def print_sensor_values():
    # get sensor1's distance in cm
    distance1 = sensor1.distance_in_cm()
    # get sensor2's distance in inches
    distance2 = sensor2.distance_in_inches()

    print("Sensor1 (Metric System)", distance1, "cm")
    print("Sensor2 (Imperial System)", distance2, "inches")

# prints values every second
while(True):
    print_sensor_values()
    time.sleep(1)