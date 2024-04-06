# Task Tracker v1.2

### Description
Code Overview:
* Connect to wifi network
* Enter while loop
* Read task statuses (Use switch statuses for now)
* Set LEDs based on task statuses
* Read switch statuses
* If any switch status is toggled, send webhook with send_data
* Repeat while loop

### Instructions
1. Connect Task Tracker to PC via USB C cable
2. Open CIRCUITPY drive in file explorer
3. Open settings.toml in text editor
4. Replace your_wifi_ssid with your wifi's ssid
5. Replace your_wifi_password with your wifi's password
6. Replace your_webhook_send_url with the URL Task Tracker will post to
7. Save settings.toml
8. Eject CIRCUITPY
9. Connect Task Tracker to power


### Example Webhook Data
Sent by Task Tracker:
{
  "switch2": "False",
  "switch1": "True",
  "switch5": "False",
  "switch4": "True",
  "switch3": "True"
}
