per_cent = {}
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
ТКБ = int((per_cent['ТКБ']) * (money/100))
СКБ = int((per_cent['СКБ']) * (money/100))
ВТБ = int((per_cent['ВТБ']) * (money/100))
СБЕР = int((per_cent['СБЕР']) * (money/100))
deposit = [ТКБ, СКБ, ВТБ, СБЕР]
print("Накопления за год =", deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
print(per_cent)