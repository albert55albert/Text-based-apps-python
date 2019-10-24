import random
joc_nou = 1

while joc_nou == 1:

    pachet = []
    for culoare in ['inima rosie','inima neagra','romb','trefla']:
        for numere in ['2','3','4','5','6','7','8','9','10','A','J','Q','K']:
            pachet.append(numere + ' de ' + culoare)


    print('Blackjack.')

    print('Fiecare juctor v-a primi doua carti dupa care are voie sa mai ia si alte carti.')

    print('''
    #-----------------------------------------#
    #         JUCATORUL REAL (TU)             #
    #-----------------------------------------#

            ''')

    scor = 0
    scor2 = 0

    def verificare():
        global scor
        for elem in mana_j1:
            if elem == '2': 
                scor += 2
            elif elem == '3':
                scor += 3
            elif elem == '4':
                scor += 4
            elif elem == '5':
                scor += 5
            elif elem == '6':
                scor += 6
            elif elem == '7':
                scor += 7
            elif elem == '8':
                scor += 8
            elif elem == '9':
                scor += 9
            elif elem == '10':
                scor += 10
            elif elem == 'A':
                scor += 11
            elif elem == 'J':
                scor += 10
            elif elem == 'Q':
                scor += 10
            elif elem == 'K':
                scor += 10

    def verificare2():
        global scor2
        for elem in mana_j2:
            if elem == '2': 
                scor2 += 2
            elif elem == '3':
                scor2 += 3
            elif elem == '4':
                scor2 += 4
            elif elem == '5':
                scor2 += 5
            elif elem == '6':
                scor2 += 6
            elif elem == '7':
                scor2 += 7
            elif elem == '8':
                scor2 += 8
            elif elem == '9':
                scor2 += 9
            elif elem == '10':
                scor2 += 10
            elif elem == 'A':
                scor2 += 11
            elif elem == 'J':
                scor2 += 10
            elif elem == 'Q':
                scor2 += 10
            elif elem == 'K':
                scor2 += 10

    nimereala1 = random.choice(pachet)
    pozitie1 = pachet.index(nimereala1)
    del pachet[pozitie1]

    nimereala2 = random.choice(pachet)
    pozitie2 = pachet.index(nimereala2) 
    del pachet[pozitie2]

    mana_j1 = nimereala1 + ', ' + nimereala2
    print(scor)
    print('Acesta este mana ta: ' + mana_j1)
    print('Doresti sa mai iei inca o carte? da sau nu?')
    alegere1 = input()
    if alegere1 == 'da':
        bucla = 1
        while bucla == 1:
            nimereala3 = random.choice(pachet)
            pozitie3 = pachet.index(nimereala3)
            del pachet[pozitie3]
            
            mana_j1 = mana_j1 + ', ' + nimereala3
            print('Mana ta este: ' + mana_j1)
            print('Doresti sa mai iei inca o carte?')
            #verificare()
            alegere2 = input()
            if alegere2 == 'da':
                bucla = 1
            else:
                bucla = 0
                verificare()
                print('Cartile jucatorului 1 valoreaza:', scor)
    else:
        verificare()
        print('Cartile jucatorului 1 valoreaza:', scor)
        
    print('''

    #-----------------------------------------#
    #              CALCULATOR                 #
    #-----------------------------------------#

                         ''')

    #-----------------------------------------#
    #-----------------------------------------#
    #              JUCATOR 2                  #
    #-----------------------------------------#
    #-----------------------------------------#

    nimereala4 = random.choice(pachet)
    pozitie4 = pachet.index(nimereala4)
    del pachet[pozitie4]

    nimereala5 = random.choice(pachet)
    pozitie5 = pachet.index(nimereala5) 
    del pachet[pozitie5]

    mana_j2 = nimereala4 + ', ' + nimereala5

    verificare2()

    while 18 > scor2:
        if not scor2 >= 21:
            if not 18 > scor2 > 21 : 
                    nimereala6 = random.choice(pachet)
                    pozitie6 = pachet.index(nimereala6) 
                    del pachet[pozitie6]
                    mana_j2 = mana_j2 + ', ' + nimereala6
                    verificare2()
    print('Mana calculatorului este: ' + mana_j2)
    print('Cartile calculatorului valoreaza:', scor2)
    print('')


    if scor > scor2 and scor <= 21:
        print('Tu ai castigat!')
    elif scor2 > scor and scor2 <= 21:
        print('Calculatorul a castigat!')
    elif scor == scor2 and scor <= 21 and scor2 <= 21:
        print('Egal!')
    elif scor2 > scor and scor2 > 21 and scor < 21:
        print('Tu ai castigat!')
    elif scor > scor2 and scor > 21 and scor2 < 21:
        print('Calculatorul a castigat!')
    elif scor > 21 and scor2 > 21:
        print('Nu a castigat nimeni.')

    print('')
    print('Doresti sa mai joci? da sau nu?')
    dorinta = input()
    if dorinta == 'da':
        joc_nou = 1
    else:
        joc_nou = 0
        print('Imi pare rau ca nu doresti sa mai joci.')
        print('')



