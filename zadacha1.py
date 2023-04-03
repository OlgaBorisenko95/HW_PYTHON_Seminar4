#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
#m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

amount1=(int(input("Кол-во элементов первого множества: ")))
list_1=[]
for i in range(amount1):
    numbers = int(input("Введите числа "))
    list_1.append(numbers)
print(list_1)


amount2=(int(input("Кол-во элементов второго множества: ")))
list_2 = []
for i in range(amount2):
    numbers = int(input("Введите числа "))
    list_2.append(numbers)
print(list_2)


num_list3 = list_1+list_2

checked_nums_list = []
for i in num_list3:
    if num_list3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
        print(i)