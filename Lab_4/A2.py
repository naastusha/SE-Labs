def draw_rectangle(rows, columns, ch):
    print(f'ПРЯМОУГОЛЬНИК {rows} x {columns}:')
    for i in range (rows):
        for j in range (columns):
            print (ch, end='')
        print()

def draw_triangle(rows, ch):
    print(f"ПРАВЫЙ ТРЕУГОЛЬНИК:")
    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end='')
        print()

def draw_frame (rows, columns, ch):
    print(f"РАМКА {rows} x {columns}:")
    for i in range(rows):
        for j in range (columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(" ", end='')
        print()

rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
ch = input("Введите символ для изображения: ")
draw_rectangle(rows, columns, ch)
print()
draw_triangle(rows, ch)
print()
draw_frame(rows, columns, ch)