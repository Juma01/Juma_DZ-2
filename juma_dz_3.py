# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

""" Список и словарь """

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: {'December', 'January', 'February'},
                2: {'March', 'April', 'May'},
                3: {'June', 'July', 'August'},
                4: {'September', 'October', 'November'},
                }

num = int(input("Введите число месяца:"))
if num == 12 or num == 1 or num == 2:
    print(seasons_list[0])
    print(f"Зима", seasons_dict.get(1))
elif num == 3 or num == 4 or num == 5:
    print(seasons_list[1])
    print(f"Весна", seasons_dict.get(2))
elif num == 6 or num == 7 or num == 8:
    print(seasons_list[2])
    print(f"Лето", seasons_dict.get(3))
elif num == 9 or num == 10 or num == 11:
    print(seasons_list[3])
    print(f"Осень", seasons_dict.get(4))
else:
    print("Ввели не коректное число!")

""" Словарь в списке """

seasons = [
    {1: ['December', 'January', 'February']},
    {2: ['March', 'April', 'May']},
    {3: ['June', 'July', 'August']},
    {4: ['September', 'October', 'November']},
          ]

num = int(input("Введите число месяца от 1 до 12: "))
if num == 1 or num == 2 or num == 12:
    print(f"Зима", seasons[0].get(1))
elif num == 3 or num == 4 or num == 5:
    print(f"Весна", seasons[1].get(2))
elif num == 6 or num == 7 or num == 8:
    print(f"Лето", seasons[2].get(3))
elif num == 9 or num == 10 or num == 11:
    print(f"Осень", seasons[3].get(4))
else:
    print(f"Вы ввели не коректное число ")
