# 1. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.​Пример:​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​

#from random import randint
#
#listnum = []
#for i in range(randint(3, 10)): 
#    listnum.append(randint(0, 20))
#
#print(f'Generated list: {listnum}')
#
#uniclist = list(filter((lambda i: listnum.count(i) == 1), listnum))
#
#print(f'List of unique elements: {uniclist}')

# 2. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#num = int(input('Enter the number: '))
#
#binarylist = list(range(-10, 1))
#binarynum = list(map(lambda i: num//2**abs(i)%2, binarylist))
#print(*binarynum)

# 3. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#N = int(input('Enter the number: '))
#x = lambda a, b:  a * b
#f = 1
#for i in range(N):
#    i+=1
#    f = x(f,i)
#    print(f, end=' ')

# 4. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#from random import randint
#
#list = []
#for i in range(randint(3, 7)): 
#    list.append(randint(0, 20))
#
#print(f'Generated list: {list}')
#print(f'The sum of the elements in odd positions: {sum(list[1::2])}')

# 5. Реализуйте алгоритм перемешивания списка.

#from random import Random, randint
#
#N = int(input('Enter the number: '))
#numbers = [randint(-N,N+1) for i in range(N)]
#print('Original list: ', numbers)
#
#def mix(numbers):
#    list = numbers[:]
#    numbers_length = len(list)
#    for i in range(numbers_length):
#        index = randint(0, numbers_length - 1)
#        temp = list[i]
#        list[i] = list[index]
#        list[index] = temp
#    return list
#print('Mixed list: ', mix(numbers))