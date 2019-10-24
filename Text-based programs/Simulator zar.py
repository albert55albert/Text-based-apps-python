from random import randint

a = randint(1, 6)

print("Dice simulator")
print("Numarul care l-ai dat cu zarul este:", a)
print("Vrei sa mai dai odata cu zarul?")

a = randint(1, 6)

if input() == 'da':
        print("Numarul care l-ai dat dinou cu zarul este:", a)
else:
        print("Imi pare rau !")
