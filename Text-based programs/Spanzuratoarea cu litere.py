import random

cuvinte = ['mar', 'par', 'cais', 'prun', 'nuc']

cuvant = random.choice(cuvinte)
iesire = '_' * len(cuvant)
lista1 = list(cuvant)
mega = list(iesire)
incercari = len(cuvant) + 3
ghicite = []


print('Bine ai venit la Spanzuratoarea cu litere.')
print('')
print(mega)
print('INDICIU: Cuvantul incepe cu litera', cuvant[0], '.')

while incercari > 0:
    print('Introdu o litera care crezi ca se afla in cuvant.')
    ghicire = input()
    #print(ghicite)
    if ghicire in cuvant:
        if ghicire not in ghicite:
            pozitie_ghicire = lista1.index(ghicire)
            mega[pozitie_ghicire] = ghicire
            print(mega)
            ghicite.append(ghicire)
            if lista1 == mega:
                print('Bravo ai ghicit cuvantul')
                break
            elif incercari == -1 and lista1 != mega:
                print('Ai pierdut!')
        else:
            print('Ai introdus o litera pe care ai ghicit.o.')
            
    else:
        print('Litera', ghicire, 'nu se afla in cuvant.')
        print(mega)
        incercari = incercari-1
        print('Mai ai', incercari, 'incercari.')
        if incercari == -1 and lista1 != mega:
            print('Ai pierdut!')
