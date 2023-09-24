# Вводить в бесконечном цикле зарплаты сотрудников
# Окончание ввода - ввод 0.
# После чего напечатать среднюю зарплату.
lst = []
while True:
    i = int(input())
    if i == 0: break
    lst.append(int(i))
print (sum(lst)/len(lst))