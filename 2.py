""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. """

n = int(input())
list_simple = []
i = 2
while n > 1:
    if n % i == 0:
        list_simple.append(i)
        n = n/i
    else:
        i += 1
print(list_simple)