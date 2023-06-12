#Код для подсчета заработной платы в зависимости от отработанных часов

# Ввод размера часовой ставки
stavka = input ("Размер почасовой ставки: ")
stavka = int(stavka)

# Ввод количества рабочих часов
hours = input("Введите количество будних часов: ")
h = int(hours)
whours = input("Введите количество выходных часов: ")
wh = int(whours)
h = h + (wh * 2)

# Ввод процента северных надбавок
severnie = input ("Введите процент северных надбавок: ")
sev = int(severnie) * 0.01

# Ввод премии
premiya = input ("Введите сумму премии: ")
prm = int(premiya)

# Вычисление зарплаты
oplata_po_chasam = stavka * h

rk = (oplata_po_chasam + prm) * 0.7  # Районный коэффициент
sn = (oplata_po_chasam + prm) * sev  # Северные надбавки
dolg = (oplata_po_chasam + prm + rk + sn)  # Долг предприятия
nalog = 0.13 * dolg  # НДФЛ
zp = dolg - nalog  # Итоговая сумма

# Вывод результатов
print("Оплата по часовому тарифу =", round(oplata_po_chasam, 2))
print("Районный коэффициент =", round(rk, 2))
print("Северные надбавки =", round(sn, 2))
print("Премия =", round(prm, 2))
print("Долг предприятия на месяц =", round(dolg, 2))
print("Налог =", round(nalog, 2))
print("Зарплата =", round(zp, 2))
