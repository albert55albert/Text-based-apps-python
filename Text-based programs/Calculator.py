#Programul face operatii simple , poate sa adune sa scada sa imparta si sa inmulteasca .

#Aceasta functie face suma a doua numere .
def add(x, y):
   return x + y

#Aceasta functie face scaderea a doua numere .
def subtract(x, y):
   return x - y

#Aceasta functie inmulteste doua numere .
def multiply(x, y):
   return x * y

#Aceasta functie imparte doua numere .
def divide(x, y):
   return x / y

print("Selecteaza operatia.")
print("1.Adunare")
print("2.Scadere")
print("3.Inmultire")
print("4.Impartire")

#Ia o valoare de la utilizator . 
choice = input("Introdu alegerea(1/2/3/4):")

num1 = int(input("Introdu primul numar: "))
num2 = int(input("Introdu al doilea numar: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Comanda invalida !")
