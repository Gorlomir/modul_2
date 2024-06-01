#while True:
    #number = int(input("Введите число: "))
    #if number % 2 == 0 :
        #print("Число чётное")
       # continue
    #else:
        #print("Число нечётное")
        #break
#print("Я за циклом")
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
индекс = 0
while индекс < len(my_list) and my_list[индекс] >= 0:
    print(my_list[индекс])
    индекс += 1



