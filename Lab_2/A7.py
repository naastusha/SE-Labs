x1 = int(input("Введите координату по x первой клетки: "))
y1 = int(input("Введите координату по y первой клетки: "))
x2 = int(input("Введите координату по x второй клетки: "))
y2 = int(input("Введите координату по y второй клетки: "))
cletka1 = (x1 + y1) % 2
cletka2 = (x2 + y2) % 2
if cletka1 == cletka2:
    print("YES")

    if cletka1 == 0:
        print("White")
    else:
        print ("Black")

else:
    print("NO")