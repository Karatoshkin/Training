month= {
  1:"Январь",
  2:"Февраль",
  3:"Март",
  4:"Апрель",
  5:"Май",
  6:"Июнь",
  7:"Июль",
  8:"Август",
  9:"Сентябрь",
  10:"Октябрь",
  11:"Ноябрь",
  12:"Декабрь"
}

print ("Укажите месяц")
def seasons(number_of_month):
  if number_of_month in range (3, 5):
    print (f"Вы указали {month[number_of_month]} - Весна")
  elif number_of_month in range (6, 8):
    print (f"Вы указали {month[number_of_month]} - Лето")
  elif number_of_month in range (9, 11):
    print (f"Вы указали {month[number_of_month]} - Осень")
  elif number_of_month in (12, 1, 2):
    print (f"Вы указали {month[number_of_month]} - Зима")
  else:
    print (f"Ты чё ебанутый? Тебе сказали номер месяца, у нас что, есть {number_of_month}-ый месяц??")

seasons(2)