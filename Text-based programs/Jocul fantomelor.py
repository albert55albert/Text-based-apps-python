#Jocul fantomleor
from random import randint
print("Jocul fantomelor")
feeling_brave = True
score = 0
while feeling_brave:
	ghost_door = randint(1, 3)
	print("Exista trei usi...")
	print("In spatele uneia se afla o fantoma...")
	print("Ce usa doresti sa deschizi ?")
	door = input ("1, 2 sau 3 ?")
	door_num = int(door)
	if door_num == int(door):
		print("FANTOMA !")
		feeling_brave = False
	else:
		print("Nicio fantoma !")
		print("Ai intrat in camera urmatoare.")
		score = score + 1
print("Fugi !")
print("Ai pierdut ! Scorul tau este :", score)
