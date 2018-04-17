import urllib.request
import time
import pygame
import json

pygame.init()
baah = pygame.mixer.Sound("baaah.wav")

with urllib.request.urlopen("https://blockchain.info/ticker") as output:
    response = json.loads(output.read().decode('utf-8'))

base_amount = response["USD"]["15m"]

print("\n\nBase amount: ${}\n\n".format(base_amount))

interval = int(input("Enter the time interval for performing the check (seconds): "))

with urllib.request.urlopen("https://blockchain.info/ticker") as output:
    current_response = json.loads(output.read().decode('utf-8'))
current_amount = current_response["USD"]["15m"]

while True:

    percentage_change = (current_amount - base_amount)/base_amount
    print("Deviation from base amount: {}% ------- ${}".format(percentage_change, current_amount))
    if percentage_change > 0.00010 or percentage_change < -0.00010:
        baah.play()
    with urllib.request.urlopen("https://blockchain.info/ticker") as output:
        current_response = json.loads(output.read().decode('utf-8'))
    current_amount = current_response["USD"]["15m"]
    time.sleep(interval)
