 #Требуется вычислить, сколько раз встречается некоторое число X в 
#массиве A[1..N]. Пользователь в первой строке вводит натуральное число
#N – количество элементов в массиве. В последующих  строках записаны N 
#целых чисел Ai. Последняя строка содержит число X

#*Пример:*
#5
#    1 2 3 4 5
#    3
#    -> 1

N = int(input("Размер списка: ")) 
N = range(N)
x = int(input("Число x: "))
count = 0

for i in (N):
    if i == x:
        count += 1
else:
    print("x", count) 
for i in N:    
    print(i)           

 #Требуется найти в массиве A[1..N] самый близкий по величине элемент 
 # к заданному числу X. Пользователь в первой строке вводит натуральное
 #  число N – количество элементов в массиве. В последующих  строках 
 # записаны N целых чисел Ai. Последняя строка содержит число X

#*Пример:*

#5
#    1 2 3 4 5
#    6
#    -> 5
N = int(input("Размер списка: ")) 
N = range(N + 1)
x = int(input("Число x: "))
for i in N:    
    print(i)

num = N[0]
for i in N:
    if abs(i - x)  <  abs(num - x) :
        num = num + 1
else:
    
    print("x", num ) #*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность. В случае с английским алфавитом очки 
# распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы 
# оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
#  Напишите программу, которая вычисляет стоимость введенного 
# пользователем слова. Будем считать, что на вход подается только одно 
# слово, которое содержит либо только английские, либо только русские
#  буквы.

#*Пример:*

#ноутбук
#    12 
#    
list_1 = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 
 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ' }
list_2 = {1:'AEIOULNSTR' , 2:'DG' , 3:'BCMP', 4:'FHVWY', 
5:'K', 8:'JX', 10:'QZ'}          
text = input('Введите слово: ')
result = [key for letter in text for key, value in list_1.items() if letter in value] 

print(sum(result))


        
   
