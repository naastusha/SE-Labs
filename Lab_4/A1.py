import random
import time
n = int(input('Введите количество примеров: '))
correct_count = 0
total_time = 0.0
for i in range (1, n + 1):
    a = random.randint(2,9)
    b = random.randint(2, 9)
    correct_answer = a * b
    print(f"Вопрос {i}/{n}")
    start_time = time.time()
    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    time_spend = time.time() - start_time
    total_time += time_spend
    if answer == correct_answer:
        print(f"Верно! (Время: {time_spend:.1f} сек)")
        correct_count += 1
    else:
        print(f"Неверно! Правильно: {correct_answer} (Время: {time_spend:.1f} сек)")

print("=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
if n>0:
    average_time = total_time / n
else:
    average_time = 0.0

print(f"Среднее время на вопрос: {average_time:.1f} сек")
print(f"Правильных ответов: {correct_count}/{n}")
if n > 0:
    percent = (correct_count / n) * 100
    print(f"Процент правильных: {percent:.1f}%")
else:
    print("Процент правильных: 0.0%")
