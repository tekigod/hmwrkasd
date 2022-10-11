# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def numberList(n,qwe):
    for i in range(2,n+1):
        if i==n: 
            qwe.append(i)
            break
        if not n%i: 
            qwe.append(i) 
            numberList(n//i,qwe) 
            break



asd=int(input('Введите число: '))
qwe=[]

numberList(asd,qwe)

print(f'Состав простых множителей числа {asd}: \n{qwe}')