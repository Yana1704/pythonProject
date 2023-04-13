all_tickets = int(input("Введите количество билетов "))
discount = int(input("При покупке от 4-х билетов действует скидка 10% от стоимости заказа!"))
age = list(map(int, input("Введите через пробел возраст посетителей ").split()))
while all_tickets != len(age):
    age = list(map(int, input("Количество введенных билетов не совпадает с количеством посетителей\n""Введите через пробел возраст посетителей").split()))
price_tickets = []
for i in age:
    if i in range(0, 18):
        price_tickets.append(0)
    elif i in range(18, 25):
        price_tickets.append(990)
    else:
        price_tickets.append(1390)
        if all_tickets > 3:
            print("Сумма к оплате с учетом скидки составляет: ", sum(price_tickets) - ((sum(price_tickets)/100)*10),"рублей")
        else:
            print("Сумма к оплате составляет: ", sum(price_tickets), "рублей")
