pred = int(input('Введите показания предыдущего месяца: '))
tek = int(input('Введите показания текущего месяца: '))
if tek >= pred:
    gaz = tek - pred
else:
    gaz = (10000 - pred) + tek
if gaz <= 300:
    cena = 21
elif gaz <= 600:
    cena = 21 + (gaz - 300) * 0.06
elif gaz <= 800:
    cena = 21 + 300 * 0.06 + (gaz - 600) * 0.04
elif gaz > 800:
    cena = 21 + 300 * 0.06 + 200 * 0.04 + (gaz - 800) * 0.025
cena += 0.00001
sredn_cena = cena / gaz
print (f"{'Предыдущее':^12} {'Текущее':^12} {'Использовано':^12} {'К оплате':^12} {'Ср. цена m^3':^12}")
print (f"{pred:^12} {tek:^12} {gaz:^12} {cena:^12.2f} {sredn_cena:^12.2f}")
