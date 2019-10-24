#Piatra, Hartie, Foarfeca | VS. calculator
import random

print('Piatra, Hartie, Foarfeca VS calculator')
print('(scorul tau) - (scorul calculatorului)')
print('Doresti sa joci?')

loop = 1
loop1 = 1

score_pc = 0
score_juc = 0

dorinta = input()
while loop1 == 1:
    
    if dorinta == 'da':
        print('Alege-ti optiunea (piatra/foarfeca/hartie):')

        lista_pos = ['piatra', 'hartie', 'foarfeca']

        alegere_pc = random.choice(lista_pos)

        alegere_0 = input()

        joc = True
    
        while joc:
            if alegere_0 == alegere_pc:
                print('Egal.')
                print('Scorul este ', score_juc, '- ', score_pc)
                break
            elif alegere_0 == 'piatra':
                if alegere_pc == lista_pos[2]:
                    print('Ai castigat, calculatorul a ales', alegere_pc)
                    score_juc += 1
                    print('Scorul este ', score_juc, '- ', score_pc)
                    break
                else:
                    print('Ai pierdut, calculatorul a ales', alegere_pc)
                    score_pc += 1
                    print('Scorul este ', score_juc, '- ', score_pc)
                    break
            elif alegere_0 == 'hartie':
                if alegere_pc == lista_pos[0]:
                    print('Ai castigat, caluclatorul a ales', alegere_pc)
                    score_juc += 1
                    print('Scorul este ', score_juc, '- ', score_pc)
                    break
                else:
                    print('Ai pierdut, calculatorul a ales', alegere_pc)
                    score_pc += 1
                    print('Scorul este ', score_juc, '- ', score_pc)
                    break
            elif alegere_0 == 'foarfeca':
                if alegere_pc == lista_pos[1]:
                    print('Ai castigat, calculatorul a ales', alegere_pc)
                    score_juc += 1
                    print('Scorul este ', score_juc, '- ', score_pc)
                    break
                else:
                    print('Ai pierdut, calculatorul a ales', alegere_pc)
                    score_pc += 1
                    print('Scorul este ', score_juc, '- ', score_pc)
                    break
        print('Doresti sa mai joci?')
        dorinta1 = input()
        if dorinta1 == 'da':
            continue
        else:
            print('Ok')
            print('Scorul este ', score_juc, '- ', score_pc)
            break

    else:
        print('Imi pare rau ca nu ati dorit sa jucati.')
