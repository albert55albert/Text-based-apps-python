import random

pachet = ['2 de inima rosie', '3 de inima rosie', '4 de inima rosie', '5 de inima rosie', '6 de inima rosie', '7 de inima rosie', 
            '8 de inima rosie', '9 de inima rosie', '10 de inima rosie', 'A de inima rosie', 'J de inima rosie', 'Q de inima rosie',
            'K de inima rosie', '2 de inima neagra', '3 de inima neagra', '4 de inima neagra', '5 de inima neagra', '6 de inima neagra', '7 de inima neagra', 
            '8 de inima neagra', '9 de inima neagra', '10 de inima neagra', 'A de inima neagra', 'J de inima neagra', 'Q de inima neagra',
            'K de inima neagra', '2 de trefla', '3 de trefla', '4 de trefla', '5 de trefla', '6 de trefla','7 de trefla', '8 de trefla', 
            '9 de trefla', '9 de trefla', 'A de trefla', 'J de trefla', 'Q de trefla','K de trefla', '2 de romb', '3 de romb', '4 de romb', '5 de romb', 
            '6 de romb', '7 de romb', '8 de romb', '9 de romb', '10 de romb', 'A de romb', 'J de romb', 'Q de romb','K de romb']

print('Blackjack.')
print('Fiecare juctor v-a primi doua carti dupa care are voie sa mai ia.')

scor = 0

nimereala1 = random.choice(pachet)
#----------------# Verificare

if nimereala1 == '2 de inima rosie' or nimereala1 == '2 de inima neagra' or nimereala1 == '2 de trefla' or nimereala1 == '2 de romb':
    scor += 2
elif nimereala1 == '3 de inima rosie' or nimereala1 == '3 de inima neagra' or nimereala1 == '3 de trefla' or nimereala1 == '3 de romb':
    scor += 3
elif nimereala1 == '4 de inima rosie' or nimereala1 == '4 de inima neagra' or nimereala1 == '4 de trefla' or nimereala1 == '4 de romb':
    scor += 4
elif nimereala1 == '5 de inima rosie' or nimereala1 == '5 de inima neagra' or nimereala1 == '5 de trefla' or nimereala1 == '5 de romb':
    scor += 5
elif nimereala1 == '6 de inima rosie' or nimereala1 == '6 de inima neagra' or nimereala1 == '6 de trefla' or nimereala1 == '6 de romb':
    scor += 6
elif nimereala1 == '7 de inima rosie' or nimereala1 == '7 de inima neagra' or nimereala1 == '7 de trefla' or nimereala1 == '7 de romb':
    scor += 7
elif nimereala1 == '8 de inima rosie' or nimereala1 == '8 de inima neagra' or nimereala1 == '8 de trefla' or nimereala1 == '8 de romb':
    scor += 8
elif nimereala1 == '9 de inima rosie' or nimereala1 == '9 de inima neagra' or nimereala1 == '9 de trefla' or nimereala1 == '9 de romb':
    scor += 9
elif nimereala1 == '10 de inima rosie' or nimereala1 == '10 de inima neagra' or nimereala1 == '10 de trefla' or nimereala1 == '10 de romb':
    scor += 10
elif nimereala1 == 'A de inima rosie' or nimereala1 == 'A de inima neagra' or nimereala1 == 'A de trefla' or nimereala1 == 'A de romb':
    scor += 11
elif nimereala1 == 'J de inima rosie' or nimereala1 == 'J de inima neagra' or nimereala1 == 'J de trefla' or nimereala1 == 'J de romb':
    scor += 10
elif nimereala1 == 'Q de inima rosie' or nimereala1 == 'Q de inima neagra' or nimereala1 == 'Q de trefla' or nimereala1 == 'Q de romb':
    scor += 10
elif nimereala1 == 'K de inima rosie' or nimereala1 == 'K de inima neagra' or nimereala1 == 'K de trefla' or nimereala1 == 'K de romb':
    scor += 10

#-----------------# Verificare stop
pozitie1 = pachet.index(nimereala1)
del pachet[pozitie1]

nimereala2 = random.choice(pachet)
#--------------# Verificare 2

if nimereala2 == '2 de inima rosie' or nimereala2 == '2 de inima neagra' or nimereala2 == '2 de trefla' or nimereala2 == '2 de romb':
    scor += 2
elif nimereala2 == '3 de inima rosie' or nimereala2 == '3 de inima neagra' or nimereala2 == '3 de trefla' or nimereala2 == '3 de romb':
    scor += 3
elif nimereala2 == '4 de inima rosie' or nimereala2 == '4 de inima neagra' or nimereala2 == '4 de trefla' or nimereala2 == '4 de romb':
    scor += 4
elif nimereala2 == '5 de inima rosie' or nimereala2 == '5 de inima neagra' or nimereala2 == '5 de trefla' or nimereala2 == '5 de romb':
    scor += 5
elif nimereala2 == '6 de inima rosie' or nimereala2 == '6 de inima neagra' or nimereala2 == '6 de trefla' or nimereala2 == '6 de romb':
    scor += 6
elif nimereala2 == '7 de inima rosie' or nimereala2 == '7 de inima neagra' or nimereala2 == '7 de trefla' or nimereala2 == '7 de romb':
    scor += 7
elif nimereala2 == '8 de inima rosie' or nimereala2 == '8 de inima neagra' or nimereala2 == '8 de trefla' or nimereala2 == '8 de romb':
    scor += 8
elif nimereala2 == '9 de inima rosie' or nimereala2 == '9 de inima neagra' or nimereala2 == '9 de trefla' or nimereala2 == '9 de romb':
    scor += 9
elif nimereala2 == '10 de inima rosie' or nimereala2 == '10 de inima neagra' or nimereala2 == '10 de trefla' or nimereala2 == '10 de romb':
    scor += 10
elif nimereala2 == 'A de inima rosie' or nimereala2 == 'A de inima neagra' or nimereala2 == 'A de trefla' or nimereala2 == 'A de romb':
    scor += 11
elif nimereala2 == 'J de inima rosie' or nimereala2 == 'J de inima neagra' or nimereala2 == 'J de trefla' or nimereala2 == 'J de romb':
    scor += 10
elif nimereala2 == 'Q de inima rosie' or nimereala2 == 'Q de inima neagra' or nimereala2 == 'Q de trefla' or nimereala2 == 'Q de romb':
    scor += 10
elif nimereala2 == 'K de inima rosie' or nimereala2 == 'K de inima neagra' or nimereala2 == 'K de trefla' or nimereala2 == 'K de romb':
    scor += 10

#---------------# Verificare 2 stop
pozitie2 = pachet.index(nimereala2) 
del pachet[pozitie2]

#print(pachet)
mana_j1 = nimereala1 + ', ' + nimereala2
print('Acesta este mana jucatorului unu: ' + mana_j1)
print('Momentan cartile tale valoreaza:', scor)
print('Doresti sa mai iei inca o carte? da sau nu?')
alegere1 = input()
if alegere1 == 'da':
    bucla = 1
    while bucla == 1:
        nimereala3 = random.choice(pachet)
        #---------------# Verificare 3
        if nimereala3 == '2 de inima rosie' or nimereala3 == '2 de inima neagra' or nimereala3 == '2 de trefla' or nimereala3 == '2 de romb':
            scor += 2
        elif nimereala3 == '3 de inima rosie' or nimereala3 == '3 de inima neagra' or nimereala3 == '3 de trefla' or nimereala3 == '3 de romb':
            scor += 3
        elif nimereala3 == '4 de inima rosie' or nimereala3 == '4 de inima neagra' or nimereala3 == '4 de trefla' or nimereala3 == '4 de romb':
            scor += 4
        elif nimereala3 == '5 de inima rosie' or nimereala3 == '5 de inima neagra' or nimereala3 == '5 de trefla' or nimereala3 == '5 de romb':
            scor += 5
        elif nimereala3 == '6 de inima rosie' or nimereala3 == '6 de inima neagra' or nimereala3 == '6 de trefla' or nimereala3 == '6 de romb':
            scor += 6
        elif nimereala3 == '7 de inima rosie' or nimereala3 == '7 de inima neagra' or nimereala3 == '7 de trefla' or nimereala3 == '7 de romb':
            scor += 7
        elif nimereala3 == '8 de inima rosie' or nimereala3 == '8 de inima neagra' or nimereala3 == '8 de trefla' or nimereala3 == '8 de romb':
            scor += 8
        elif nimereala3 == '9 de inima rosie' or nimereala3 == '9 de inima neagra' or nimereala3 == '9 de trefla' or nimereala3 == '9 de romb':
            scor += 9
        elif nimereala3 == '10 de inima rosie' or nimereala3 == '10 de inima neagra' or nimereala3 == '10 de trefla' or nimereala3 == '10 de romb':
            scor += 10
        elif nimereala3 == 'A de inima rosie' or nimereala3 == 'A de inima neagra' or nimereala3 == 'A de trefla' or nimereala3 == 'A de romb':
            scor += 11
        elif nimereala3 == 'J de inima rosie' or nimereala3 == 'J de inima neagra' or nimereala3 == 'J de trefla' or nimereala3 == 'J de romb':
            scor += 10
        elif nimereala3 == 'Q de inima rosie' or nimereala3 == 'Q de inima neagra' or nimereala3 == 'Q de trefla' or nimereala3 == 'Q de romb':
            scor += 10
        elif nimereala3 == 'K de inima rosie' or nimereala3 == 'K de inima neagra' or nimereala3 == 'K de trefla' or nimereala3 == 'K de romb':
            scor += 10

        #---------------# Verificare 3 stop
        pozitie3 = pachet.index(nimereala3)
        del pachet[pozitie3] 
        mana_j1 = mana_j1 + ', ' + nimereala3
        print('Mana ta este: ' + mana_j1)
        print('Cartile jucatorului 1 valoreaza:', scor)
        print('Doresti sa mai iei inca o carte?')
        alegere2 = input()
        if alegere2 == 'da':
            bucla = 1
        else:
            bucla = 0

scor2 = 0

nimereala4 = random.choice(pachet)
#-------------# Verificare 4

if nimereala4 == '2 de inima rosie' or nimereala4 == '2 de inima neagra' or nimereala4 == '2 de trefla' or nimereala4 == '2 de romb':
    scor2 += 2
elif nimereala4 == '3 de inima rosie' or nimereala4 == '3 de inima neagra' or nimereala4 == '3 de trefla' or nimereala4 == '3 de romb':
    scor2 += 3
elif nimereala4 == '4 de inima rosie' or nimereala4 == '4 de inima neagra' or nimereala4 == '4 de trefla' or nimereala4 == '4 de romb':
    scor2 += 4
elif nimereala4 == '5 de inima rosie' or nimereala4 == '5 de inima neagra' or nimereala4 == '5 de trefla' or nimereala4 == '5 de romb':
    scor2 += 5
elif nimereala4 == '6 de inima rosie' or nimereala4 == '6 de inima neagra' or nimereala4 == '6 de trefla' or nimereala4 == '6 de romb':
    scor2 += 6
elif nimereala4 == '7 de inima rosie' or nimereala4 == '7 de inima neagra' or nimereala4 == '7 de trefla' or nimereala4 == '7 de romb':
    scor2 += 7
elif nimereala4 == '8 de inima rosie' or nimereala4 == '8 de inima neagra' or nimereala4 == '8 de trefla' or nimereala4 == '8 de romb':
    scor2 += 8
elif nimereala4 == '9 de inima rosie' or nimereala4 == '9 de inima neagra' or nimereala4 == '9 de trefla' or nimereala4 == '9 de romb':
    scor2 += 9
elif nimereala4 == '10 de inima rosie' or nimereala4 == '10 de inima neagra' or nimereala4 == '10 de trefla' or nimereala4 == '10 de romb':
    scor2 += 10
elif nimereala4 == 'A de inima rosie' or nimereala4 == 'A de inima neagra' or nimereala4 == 'A de trefla' or nimereala4 == 'A de romb':
    scor2 += 11
elif nimereala4 == 'J de inima rosie' or nimereala4 == 'J de inima neagra' or nimereala4 == 'J de trefla' or nimereala4 == 'J de romb':
    scor2 += 10
elif nimereala4 == 'Q de inima rosie' or nimereala4 == 'Q de inima neagra' or nimereala4 == 'Q de trefla' or nimereala4 == 'Q de romb':
    scor2 += 10
elif nimereala4 == 'K de inima rosie' or nimereala4 == 'K de inima neagra' or nimereala4 == 'K de trefla' or nimereala4 == 'K de romb':
    scor2 += 10

#-------------# Verificare 4 stop
pozitie4 = pachet.index(nimereala4)
del pachet[pozitie4]

nimereala5 = random.choice(pachet)
#-------------# Verificare 5

if nimereala5 == '2 de inima rosie' or nimereala5 == '2 de inima neagra' or nimereala5 == '2 de trefla' or nimereala5 == '2 de romb':
    scor2 += 2
elif nimereala5 == '3 de inima rosie' or nimereala5 == '3 de inima neagra' or nimereala5 == '3 de trefla' or nimereala5 == '3 de romb':
    scor2 += 3
elif nimereala5 == '4 de inima rosie' or nimereala5 == '4 de inima neagra' or nimereala5 == '4 de trefla' or nimereala5 == '4 de romb':
    scor2 += 4
elif nimereala5 == '5 de inima rosie' or nimereala5 == '5 de inima neagra' or nimereala5 == '5 de trefla' or nimereala5 == '5 de romb':
    scor2 += 5
elif nimereala5 == '6 de inima rosie' or nimereala5 == '6 de inima neagra' or nimereala5 == '6 de trefla' or nimereala5 == '6 de romb':
    scor2 += 6
elif nimereala5 == '7 de inima rosie' or nimereala5 == '7 de inima neagra' or nimereala5 == '7 de trefla' or nimereala5 == '7 de romb':
    scor2 += 7
elif nimereala5 == '8 de inima rosie' or nimereala5 == '8 de inima neagra' or nimereala5 == '8 de trefla' or nimereala5 == '8 de romb':
    scor2 += 8
elif nimereala5 == '9 de inima rosie' or nimereala5 == '9 de inima neagra' or nimereala5 == '9 de trefla' or nimereala5 == '9 de romb':
    scor2 += 9
elif nimereala5 == '10 de inima rosie' or nimereala5 == '10 de inima neagra' or nimereala5 == '10 de trefla' or nimereala5 == '10 de romb':
    scor2 += 10
elif nimereala5 == 'A de inima rosie' or nimereala5 == 'A de inima neagra' or nimereala5 == 'A de trefla' or nimereala5 == 'A de romb':
    scor2 += 11
elif nimereala5 == 'J de inima rosie' or nimereala5 == 'J de inima neagra' or nimereala5 == 'J de trefla' or nimereala5 == 'J de romb':
    scor2 += 10
elif nimereala5 == 'Q de inima rosie' or nimereala5 == 'Q de inima neagra' or nimereala5 == 'Q de trefla' or nimereala5 == 'Q de romb':
    scor2 += 10
elif nimereala5 == 'K de inima rosie' or nimereala5 == 'K de inima neagra' or nimereala5 == 'K de trefla' or nimereala5 == 'K de romb':
    scor2 += 10

#-------------# Verificare 5 stop
pozitie5 = pachet.index(nimereala5) 
del pachet[pozitie5]

mana_j2 = nimereala4 + ', ' + nimereala5
print('Acesta este mana jucatorului doi: ' + mana_j2)
print('Cartile jucatorlui 2 valoreaza:', scor2)
print('Doresti sa mai iei inca o carte? da sau nu?')
alegere3 = input()
if alegere3 == 'da':
    bucla2 = 1
    while bucla2 == 1:
        nimereala6 = random.choice(pachet)
        #-------------# Verificare 6

        if nimereala6 == '2 de inima rosie' or nimereala6 == '2 de inima neagra' or nimereala6 == '2 de trefla' or nimereala6 == '2 de romb':
            scor2 += 2
        elif nimereala6 == '3 de inima rosie' or nimereala6 == '3 de inima neagra' or nimereala6 == '3 de trefla' or nimereala6 == '3 de romb':
            scor2 += 3
        elif nimereala6 == '4 de inima rosie' or nimereala6 == '4 de inima neagra' or nimereala6 == '4 de trefla' or nimereala6 == '4 de romb':
            scor2 += 4
        elif nimereala6 == '5 de inima rosie' or nimereala6 == '5 de inima neagra' or nimereala6 == '5 de trefla' or nimereala6 == '5 de romb':
            scor2 += 5
        elif nimereala6 == '6 de inima rosie' or nimereala6 == '6 de inima neagra' or nimereala6 == '6 de trefla' or nimereala6 == '6 de romb':
            scor2 += 6
        elif nimereala6 == '7 de inima rosie' or nimereala6 == '7 de inima neagra' or nimereala6 == '7 de trefla' or nimereala6 == '7 de romb':
            scor2 += 7
        elif nimereala6 == '8 de inima rosie' or nimereala6 == '8 de inima neagra' or nimereala6 == '8 de trefla' or nimereala6 == '8 de romb':
            scor2 += 8
        elif nimereala6 == '9 de inima rosie' or nimereala6 == '9 de inima neagra' or nimereala6 == '9 de trefla' or nimereala6 == '9 de romb':
            scor2 += 9
        elif nimereala6 == '10 de inima rosie' or nimereala6 == '10 de inima neagra' or nimereala6 == '10 de trefla' or nimereala6 == '10 de romb':
            scor2 += 10
        elif nimereala6 == 'A de inima rosie' or nimereala6 == 'A de inima neagra' or nimereala6 == 'A de trefla' or nimereala6 == 'A de romb':
            scor2 += 11
        elif nimereala6 == 'J de inima rosie' or nimereala6 == 'J de inima neagra' or nimereala6 == 'J de trefla' or nimereala6 == 'J de romb':
            scor2 += 10
        elif nimereala6 == 'Q de inima rosie' or nimereala6 == 'Q de inima neagra' or nimereala6 == 'Q de trefla' or nimereala6 == 'Q de romb':
            scor2 += 10
        elif nimereala6 == 'K de inima rosie' or nimereala6 == 'K de inima neagra' or nimereala6 == 'K de trefla' or nimereala6 == 'K de romb':
            scor2 += 10

        #-------------# Verificare 6 stop
        pozitie6 = pachet.index(nimereala6)
        del pachet[pozitie6] 
        mana_j2 = mana_j2 + ', ' + nimereala6
        print('Mana ta este: ' + mana_j2)
        print('Cartile jucatorului 2 valoreaza:', scor2)
        print('Doresti sa mai iei inca o carte?')
        alegere4 = input()
        if alegere4 == 'da':
            bucla2 = 1
        else:
            bucla2 = 0

#-------------# Verificare finala

if scor > scor2 and scor <= 21:
    print('Jucatorul 1 a castigat!')
elif scor2 > scor and scor2 <= 21:
    print('Jucatorul 2 a castigat!')
elif scor == scor2 and scor <= 21 and scor2 <= 21:
    print('Egal!')
elif scor > 21:
    print('Jucatorul 2 a castigat!')
elif scor2 > 21:
    print('Jucatorul 1 a castigat!')


#-------------# Verificare finala stop

# made by Albert | sh1eld