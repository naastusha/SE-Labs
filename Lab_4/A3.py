packets = input("Ввод:")
packets = packets.replace(" ", "")
if len(packets) < 5:
    print("Длина строки должна быть не менее 5 символов")
    exit()
elif not all(char in '01' for char in packets):
    print("Неверный ввод")
    exit()
print ("Общее количество пакетов: ", len(packets))
print("Общее количество потерянных пакетов: ", packets.count('0'))
max_posl = 0
current_posl = 0
for packet in packets:
    if packet == '0':
        current_posl += 1
        if current_posl > max_posl:
            max_posl = current_posl
    else:
        current_posl = 0
print("Длина самой длинной последовательности потерянных пакетов: ", max_posl)
percent = (packets.count('0') / len(packets)) * 100
print(f"Процент потерь: {percent:.1f}%")
if percent < 1:
    print("Качество связи: отличное качество")
elif percent < 5:
    print("Качество связи: хорошее качество")
elif percent < 10:
    print("Качество связи: удовлетворительное качество")
elif percent < 20:
    print("Качество связи: плохое качество")
else:
    print("Качество связи: критическое состояние сети")

