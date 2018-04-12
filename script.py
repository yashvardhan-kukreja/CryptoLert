import requests
import time
import pygame
pygame.init()

baah = pygame.mixer.Sound("baaah.wav")

response = requests.get("https://blockchain.info/ticker").json()

base_amount = response["USD"]["15m"]

print("\n\nBase amount: $" + str(base_amount) + "\n\n")

interval = int(input("Enter the time interval for performing the check (seconds): "))

current_response = requests.get("https://blockchain.info/ticker").json()
current_amount = current_response["USD"]["15m"]

while True:

    percentage_change = (float(current_amount) - float(base_amount)) / float(base_amount)
    print("Deviation from base amount: " + str(percentage_change) + "%" + " ------- $" + str(current_amount))
    if percentage_change > 0.00010 or percentage_change < -0.00010:
        baah.play()
    current_response = requests.get("https://blockchain.info/ticker").json()
    current_amount = current_response["USD"]["15m"]
    time.sleep(interval)
