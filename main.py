number = input("Введите трехзначное число: ")
number = int(number)
s = number%10
n = number//100
m = number//10%10
print(m+n+s)