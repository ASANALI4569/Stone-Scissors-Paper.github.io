#Игра "Камень, Ножницы, Бумага"

import random

print("Давай поиграем в Камень, Ножницы, Бумага")
print("Ввод только С БОЛЬШОЙ БУКВЫ")
a=str(input("Камень, Ножницы или Бумага:"))

b=random.randint(1, 3)
if b==1:
    b=str("Камень")
    print(b)

elif b==2:
    b=str("Ножницы")
    print(b)

else:
    b=("Бумага")
    print(b)

if a==b:
    print("Ничья")

if a==str("Бумага") and b==str("Камень"):
    print("Ты выиграл(а)")

if a==str("Бумага") and b==str("Ножницы"):
    print("Ты проиграл(а)")

if a==str("Ножницы") and b==str("Бумага"):
    print("Ты выиграл(а)")

if a==str("Ножницы") and b==str("Камень"):
    print("Ты проиграл(а)")

if a==str("Камень") and b==str("Бумага"):
    print("Ты проиграл(а)")

if a==str("Камень") and b==str("Ножницы"):
    print("Ты выиграл(а)")

input()