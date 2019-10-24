bucla = 1

while bucla == 1:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def tabla():
        #print(' %c | %c | %c ' % (board[1], board[2], board[3]))
        print(board[0], ' |', board[1], '|', board[2])
        print('___|___|___')
        print(board[3], ' |', board[4], '|', board[5])
        print('___|___|___')
        print(board[6], ' |', board[7], '|', board[8])
        print('   |   |   ')
        print('')

    def tabla_ins():
        print('1', ' |', '2', '|', '3')
        print('___|___|___')
        print('4', ' |', '5', '|', '6')
        print('___|___|___')
        print('7', ' |', '8', '|', '9')
        print('   |   |   ')
        print('')

    def alegere_x():
        introducere_1 = input()
        if introducere_1 == '1':
            board[0] = 'x'
            tabla()
        elif introducere_1 == '2':
            board[1] = 'x'
            tabla()
        elif introducere_1 == '3':
            board[2] = 'x'
            tabla()
        elif introducere_1 == '4':
            board[3] = 'x'
            tabla()
        elif introducere_1 == '5':
            board[4] = 'x'
            tabla()
        elif introducere_1 == '6':
            board[5] = 'x'
            tabla()
        elif introducere_1 == '7':
            board[6] = 'x'
            tabla()
        elif introducere_1 == '8':
            board[7] = 'x'
            tabla()
        elif introducere_1 == '9':
            board[8] = 'x'
            tabla()
        else:
            print('comanda necunsocuta')

    def alegere_0():
        introducere_2 = input()
        if introducere_2 == '1':
            board[0] = '0'
            tabla()
        elif introducere_2 == '2':
            board[1] = '0'
            tabla()
        elif introducere_2 == '3':
            board[2] = '0'
            tabla()
        elif introducere_2 == '4':
            board[3] = '0'
            tabla()
        elif introducere_2 == '5':
            board[4] = '0'
            tabla()
        elif introducere_2 == '6':
            board[5] = '0'
            tabla()
        elif introducere_2 == '7':
            board[6] = '0'
            tabla()
        elif introducere_2 == '8':
            board[7] = '0'
            tabla()
        elif introducere_2 == '9':
            board[8] = '0'
            tabla()
        else:
            print('comanda necunoscuta')

    print('X si 0 -> 2 jucatori reali')
    print('')
    print('Instructiuni:')
    print('')
    print('Pentru a alege o pozitie scrii cifra corespunzatoare pozitiei.')
    print('')
    print('Pozitiile pe tabla sunt ca si in tabelul urmator:')
    print('')
    tabla_ins()


    joc = 1
    while joc == 1:
        print('Randul lui x. Scrie pozitia pe care doresti ca sa fie x:')
        alegere_x()
        print('Randul lui 0. Scrie pozitia pe care doresti ca sa fie 0:')
        alegere_0()
        print('Randul lui x. Scrie pozitia pe care doresti ca sa fie x:')
        alegere_x()
        print('Randul lui 0. Scrie pozitia pe care doresti ca sa fie 0:')
        alegere_0()
        print('Randul lui x. Scrie pozitia pe care doresti ca sa fie x:')
        alegere_x()

        variabila = 0
        if board[0] == 'x' and board[0] == board[1] and board[1] == board[2]:
            print("x a castigat")
            variabila += 1
            break
        elif board[2] == 'x' and board[2] == board[5] and board[5] == board[8]:
            print("x a castigat")
            variabila += 1
            break
        elif board[6] == 'x' and board[6] == board[7] and board[7] == board[8]:
            print("x a castigat")
            variabila += 1
            break
        elif board[0] == 'x' and board[0] == board[3] and board[3] == board[6]:
            print("x a castigat")
            variabila += 1
            break
        elif board[0] == 'x' and board[0] == board[4] and board[4] == board[8]:
            print("x a castigat")
            variabila += 1
            break
        elif board[2] == 'x' and board[2] == board[4] and board[4] == board[6]:
            print("x a castigat")
            variabila += 1
            break
        elif board[1] == 'x' and board[1] == board[4] and board[4] == board[7]:
            print("x a castigat")
            variabila += 1
            break
        elif board[3] == 'x' and board[3] == board[4] and board[4] == board[5]:
            print("x a castigat")
            variabila += 1
            break
        elif board[0] == '0' and board[0] == board[1] and board[1] == board[2]:
            print("0 a castigat")
            variabila += 1
            break
        elif board[2] == '0' and board[2] == board[5] and board[5] == board[8]:
            print("0 a castigat")
            variabila += 1
            break
        elif board[6] == '0' and board[6] == board[7] and board[7] == board[8]:
            print("0 a castigat")
            variabila += 1
            break
        elif board[0] == '0' and board[0] == board[3] and board[3] == board[6]:
            print("0 a castigat")
            variabila += 1
            break
        elif board[0] == '0' and board[0] == board[4] and board[4] == board[8]:
            print("0 a castigat")
            variabila += 1
            break
        elif board[2] == '0' and board[2] == board[4] and board[4] == board[6]:
            print("0 a castigat")
            variabila += 1
            break
        elif board[1] == '0' and board[1] == board[4] and board[4] == board[7]:
            print("0 a castigat")
            variabila += 1
            break
        elif board[3] == '0' and board[3] == board[4] and board[4] == board[5]:
            print("0 a castigat")
            variabila += 1
            break
        if variabila != 1:
            print('Randul lui 0. Scrie pozitia pe care doresti ca sa fie 0:')
            alegere_0()
            if board[0] == 'x' and board[0] == board[1] and board[1] == board[2]:
                print("x a castigat")
                variabila += 1
                break
            elif board[2] == 'x' and board[2] == board[5] and board[5] == board[8]:
                print("x a castigat")
                variabila += 1
                break
            elif board[6] == 'x' and board[6] == board[7] and board[7] == board[8]:
                print("x a castigat")
                variabila += 1
                break
            elif board[0] == 'x' and board[0] == board[3] and board[3] == board[6]:
                print("x a castigat")
                variabila += 1
                break
            elif board[0] == 'x' and board[0] == board[4] and board[4] == board[8]:
                print("x a castigat")
                variabila += 1
                break
            elif board[2] == 'x' and board[2] == board[4] and board[4] == board[6]:
                print("x a castigat")
                variabila += 1
                break
            elif board[1] == 'x' and board[1] == board[4] and board[4] == board[7]:
                print("x a castigat")
                variabila += 1
                break
            elif board[3] == 'x' and board[3] == board[4] and board[4] == board[5]:
                print("x a castigat")
                variabila += 1
                break
            elif board[0] == '0' and board[0] == board[1] and board[1] == board[2]:
                print("0 a castigat")
                variabila += 1
                break
            elif board[2] == '0' and board[2] == board[5] and board[5] == board[8]:
                print("0 a castigat")
                variabila += 1
                break
            elif board[6] == '0' and board[6] == board[7] and board[7] == board[8]:
                print("0 a castigat")
                variabila += 1
                break
            elif board[0] == '0' and board[0] == board[3] and board[3] == board[6]:
                print("0 a castigat")
                variabila += 1
                break
            elif board[0] == '0' and board[0] == board[4] and board[4] == board[8]:
                print("0 a castigat")
                variabila += 1
                break
            elif board[2] == '0' and board[2] == board[4] and board[4] == board[6]:
                print("0 a castigat")
                variabila += 1
                break
            elif board[1] == '0' and board[1] == board[4] and board[4] == board[7]:
                print("0 a castigat")
                variabila += 1
                break
            elif board[3] == '0' and board[3] == board[4] and board[4] == board[5]:
                print("0 a castigat")
                variabila += 1
                break
            if variabila != 1:
                print('Randul lui x. Scrie pozitia pe care doresti ca sa fie x:')
                alegere_x()
                if board[0] == 'x' and board[0] == board[1] and board[1] == board[2]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[2] == 'x' and board[2] == board[5] and board[5] == board[8]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[6] == 'x' and board[6] == board[7] and board[7] == board[8]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[0] == 'x' and board[0] == board[3] and board[3] == board[6]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[0] == 'x' and board[0] == board[4] and board[4] == board[8]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[2] == 'x' and board[2] == board[4] and board[4] == board[6]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[1] == 'x' and board[1] == board[4] and board[4] == board[7]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[3] == 'x' and board[3] == board[4] and board[4] == board[5]:
                    print("x a castigat")
                    variabila += 1
                    break
                elif board[0] == '0' and board[0] == board[1] and board[1] == board[2]:
                    print("0 a castigat")
                    variabila += 1
                    break
                elif board[2] == '0' and board[2] == board[5] and board[5] == board[8]:
                    print("0 a castigat")
                    variabila += 1
                    break
                elif board[6] == '0' and board[6] == board[7] and board[7] == board[8]:
                    print("0 a castigat")
                    variabila += 1
                    break
                elif board[0] == '0' and board[0] == board[3] and board[3] == board[6]:
                    print("0 a castigat")
                    variabila += 1
                    break
                elif board[0] == '0' and board[0] == board[4] and board[4] == board[8]:
                    print("0 a castigat")
                    variabila += 1
                    break
                elif board[2] == '0' and board[2] == board[4] and board[4] == board[6]:
                    print("0 a castigat")
                    variabila += 1
                    break
                elif board[1] == '0' and board[1] == board[4] and board[4] == board[7]:
                    print("0 a castigat")
                    variabila += 1
                    break
                elif board[3] == '0' and board[3] == board[4] and board[4] == board[5]:
                    print("0 a castigat")
                    variabila += 1
                    break
                if variabila != 1:
                    print('Randul lui 0. Scrie pozitia pe care doresti ca sa fie 0:')
                    alegere_0()
                    if board[0] == 'x' and board[0] == board[1] and board[1] == board[2]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[2] == 'x' and board[2] == board[5] and board[5] == board[8]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[6] == 'x' and board[6] == board[7] and board[7] == board[8]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[0] == 'x' and board[0] == board[3] and board[3] == board[6]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[0] == 'x' and board[0] == board[4] and board[4] == board[8]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[2] == 'x' and board[2] == board[4] and board[4] == board[6]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[1] == 'x' and board[1] == board[4] and board[4] == board[7]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[3] == 'x' and board[3] == board[4] and board[4] == board[5]:
                        print("x a castigat")
                        variabila += 1
                        break
                    elif board[0] == '0' and board[0] == board[1] and board[1] == board[2]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    elif board[2] == '0' and board[2] == board[5] and board[5] == board[8]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    elif board[6] == '0' and board[6] == board[7] and board[7] == board[8]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    elif board[0] == '0' and board[0] == board[3] and board[3] == board[6]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    elif board[0] == '0' and board[0] == board[4] and board[4] == board[8]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    elif board[2] == '0' and board[2] == board[4] and board[4] == board[6]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    elif board[1] == '0' and board[1] == board[4] and board[4] == board[7]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    elif board[3] == '0' and board[3] == board[4] and board[4] == board[5]:
                        print("0 a castigat")
                        variabila += 1
                        break
                    if variabila != 1:
                        print('Randul lui x. Scrie pozitia pe care doresti ca sa fie x:')
                        alegere_x()
                        if board[0] == 'x' and board[0] == board[1] and board[1] == board[2]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[2] == 'x' and board[2] == board[5] and board[5] == board[8]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[6] == 'x' and board[6] == board[7] and board[7] == board[8]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[0] == 'x' and board[0] == board[3] and board[3] == board[6]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[0] == 'x' and board[0] == board[4] and board[4] == board[8]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[2] == 'x' and board[2] == board[4] and board[4] == board[6]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[1] == 'x' and board[1] == board[4] and board[4] == board[7]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[3] == 'x' and board[3] == board[4] and board[4] == board[5]:
                            print("x a castigat")
                            variabila += 1
                            break
                        elif board[0] == '0' and board[0] == board[1] and board[1] == board[2]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        elif board[2] == '0' and board[2] == board[5] and board[5] == board[8]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        elif board[6] == '0' and board[6] == board[7] and board[7] == board[8]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        elif board[0] == '0' and board[0] == board[3] and board[3] == board[6]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        elif board[0] == '0' and board[0] == board[4] and board[4] == board[8]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        elif board[2] == '0' and board[2] == board[4] and board[4] == board[6]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        elif board[1] == '0' and board[1] == board[4] and board[4] == board[7]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        elif board[3] == '0' and board[3] == board[4] and board[4] == board[5]:
                            print("0 a castigat")
                            variabila += 1
                            break
                        else:
                            print('Egal')
                            break

    print('Doresti sa mai joci?')
    raspuns = input()
    if raspuns == 'nu':
        bucla = 0
        print('Imi pare rau ca nu doriti sa mai jucati.')
        


#made by sh1eld -> Albert
