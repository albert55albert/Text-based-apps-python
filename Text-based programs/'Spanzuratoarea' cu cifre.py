import random

print("'Spanzuratoarea' cu cifre.")
print("Doriti sa jucati? ")
dorinta = input()
if dorinta == "da":
    print('Ghiceste prima cifra:')

    nums_0 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

    nums_1 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

    nums_2 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

    x = random.choice(nums_0)

    y = random.choice(nums_1)

    z = random.choice(nums_2)

    print(str(x)+str(y)+str(z))

    print('_' * 3)

    ghicire_1 = input()

    bucla = 1
    bucla1 = 1
    bucla2 = 1


    while bucla == 1:
    
        if ghicire_1 == str(x):
            print(str(x) + '_' * 2)
            print("Ghicste a doua cifra:")
            ghicire_2 = input()
            while bucla1 == 1:
                if ghicire_2 == str(y):
                    print(str(x) + str(y) + '_')
                    print("Ghiceste a treia cifra: ")
                    ghicire_3 = input()

                    while bucla2 == 1:
                        if ghicire_3 == str(z):
                            print(str(x)+str(y)+str(z))
                            bucla = 0
                            bucla1 = 0
                            bucla2 = 0
                        else:
                            print("Mai incearca")
                            print("Tasteaza o cifra: ")
                            ghicire_3 = input()
            
                else:
                    print("Mai incearca: ")
                    print("Tasteaza o cifra: ")
                    ghicire_2 = input()
            
        elif ghicire_1 != str(x):
            print("Mai incearca")
            print("Tasteaza o cifra: ")
            ghicire_1 = input()
    print("Bravoo, ai reusit!")
    
else:
    print("Va multumim")
