# V1.2

import os
import time
import ssl
import wifi
import json
import ipaddress
import socketpool
import microcontroller
import adafruit_requests
import time
import board
import digitalio


#  connect to SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

# Ping Google as network test
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

# Configure requests
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Configure IO
switch1 = digitalio.DigitalInOut(board.GP1)
switch2 = digitalio.DigitalInOut(board.GP2)
switch3 = digitalio.DigitalInOut(board.GP3)
switch4 = digitalio.DigitalInOut(board.GP4)
switch5 = digitalio.DigitalInOut(board.GP5)
led1 = digitalio.DigitalInOut(board.GP11)
led2 = digitalio.DigitalInOut(board.GP12)
led3 = digitalio.DigitalInOut(board.GP13)
led4 = digitalio.DigitalInOut(board.GP14)
led5 = digitalio.DigitalInOut(board.GP15)
switch1.direction = digitalio.Direction.INPUT
switch1.pull = digitalio.Pull.UP
switch2.direction = digitalio.Direction.INPUT
switch2.pull = digitalio.Pull.UP
switch3.direction = digitalio.Direction.INPUT
switch3.pull = digitalio.Pull.UP
switch4.direction = digitalio.Direction.INPUT
switch4.pull = digitalio.Pull.UP
switch5.direction = digitalio.Direction.INPUT
switch5.pull = digitalio.Pull.UP
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT
led5.direction = digitalio.Direction.OUTPUT
last_switch1 = True
last_switch2 = True
last_switch3 = True
last_switch4 = True
last_switch5 = True

while True:
    try:
        # Read switch value
        switch1_read = not switch1.value
        switch2_read = not switch2.value
        switch3_read = not switch3.value
        switch4_read = not switch4.value
        switch5_read = not switch5.value

        # Read task statuses (use switch status to seed for now)
        task1 = not switch1.value
        task2 = not switch2.value
        task3 = not switch3.value
        task4 = not switch4.value
        task5 = not switch5.value

        # Set LEDs based on task statuses
        led1.value = task1
        led2.value = task2
        led3.value = task3
        led4.value = task4
        led5.value = task5

        # Check for switch change
        if (switch1_read != last_switch1) or (switch2_read != last_switch2) or (switch3_read != last_switch3) or (switch4_read != last_switch4) or (switch5_read != last_switch5):
            last_switch1, last_switch2, last_switch3, last_switch4, last_switch5 = switch1_read, switch2_read, switch3_read, switch4_read, switch5_read

            if (last_switch1 == False) or (last_switch2 == False) or (last_switch3 == False) or (last_switch4 == False) or (last_switch5 == False):
                # Send Webhook
                send_data = {
                    'switch1': str(last_switch1),
                    'switch2': str(last_switch2),
                    'switch3': str(last_switch3),
                    'switch4': str(last_switch4),
                    'switch5': str(last_switch5)
                }
                r = requests.post(os.getenv('SEND_URL'), data=json.dumps(send_data), headers={'Content-Type': 'application/json'})

        #  delays for 0.05 second
        time.sleep(0.05)
    except Exception as e:
        print("Error:\n", str(e))
        print("Resetting microcontroller in 60 seconds")
        time.sleep(60)
        microcontroller.reset()


