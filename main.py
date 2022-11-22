year_1 = int(input("Год рождения 1-го человека: "))
month_1 = int(input("Месяц рождения 1-го человека: "))
day_1 = int(input("День рождения 1-го человека: "))
year_2 = int(input("Год рождения 2-го человека: "))
month_2 = int(input("Месяц рождения 2-го человека: "))
day_2 = int(input("День рождения 2-го человека: "))
if year_1<year_2:
    print("Первый человек старше")
elif year_1>year_2:
    print("Второй человек старше")
elif year_1==year_2:
    if month_1<month_2:
        print("Первый человек старше")
    elif month_1>month_2:
        print("Второй человек старше")
    elif month_1 == month_2:
        if day_1<day_2:
            print("Первый человек старше")
        elif day_1>day_2:
            print("Второй человек старше")
        elif day_1 == day_2:
            print("Одинаковый день рождения")

