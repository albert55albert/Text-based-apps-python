from random import randint
print('Simulator de dat cu zarul.')

joc = True
loop = 1

while loop == 1:
    while joc:
        a = randint(1,6)
        print("Numarul care l-ai dat cu zarul este:", a)
        break
    print('Doresti sa mai dai inca o data?')
    dorinta1 = input()
    if dorinta1 == 'da':
        continue
    else:
        print('Ok')
        break
    
    
    
