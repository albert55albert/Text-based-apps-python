from random import randint

print('Bine ai venit la jocul comoara.')
print('Acest joc se joaca in 2 jucatori.')
print('Aceasta este harta jocului.')

print('''

       5    6    
4 @----@----@----@ 7
  |              |
  |        15    |
3 @ 14 @----@    @ 8
  |    |    |    |
  |    |   *|*   |
2 @ 13 @   *$*   @ 9
  |    |   * *   |
  |    |         |
1 @    @----@----@ 10
  |   12    11     
  |          
START

''')

avans1 = 0

avans2 = 0

print('Introdu numele primului jucator.')
num1 = input()
print('Introdu numele celui de al doilea jucator.')
num2 = input()

while True:
    print(num1, 'scrie ^zar^ pentru a da cu zarul.')
    alegere1 = input()
    if alegere1 == 'zar':
        scor1 = randint(1, 4)
        avans1 = scor1 + avans1
        print(num1, 'ai dat cu zarul numarul', scor1)
        print('Ai ajuns pe pozitia', avans1)
        print('')
        if avans1 == 16:
            print(num1, 'a castigat.')
            break
        elif avans1 >= 16:
            avans1 = avans1 - scor1
            print('Trebuia sa ai scor 16 pentru a castiga.')
        print(num2, 'scrie ^zar^ pentru a da cu zarul.')
        alegere2 = input()
        if alegere2 == 'zar':
            scor2 = randint(1, 4)
            avans2 = scor2 + avans2
            print(num2, 'ai dat cu zarul numarul', scor2)
            print('Ai ajuns pe pozitia', avans2)
            print('')
            if avans2 == 16:
                print(num2, 'a castigat.')
                break
            elif avans2 >= 16:
                avans2 = avans2 - scor2
                print('Trebuia sa ai scor 16 pentru a castiga.')
        else:
            print(num2, 'ai introdus o comanda incorecta.')
            print('Jocul se opreste deoarece ai gresit comanda!')
            break

    else:
        print(num1, 'ai introdus o comanda incorecta.')
        print('Jocul se opreste deoarece ai gresit comanda!')
        break




