money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

count = 0
money_capital = money_capital - (spend - salary)
count += 1
while spend <= money_capital + salary:
    spend *= (1+increase)
    money_capital = money_capital - (spend - salary)
    count+=1






print("Количество месяцев, которое можно протянуть без долгов:", count)
