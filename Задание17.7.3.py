per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input())
deposit = [rate*(money/100) for rate in per_cent.values()]
print(list(map(round, deposit)))
max(deposit)
Profit = "Максимальная сумма, которую вы можете заработать " + str(int(max(deposit)))
print(Profit)

