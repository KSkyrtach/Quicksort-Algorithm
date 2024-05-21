import datetime
from random import randrange

def print_list(list, index1, index2):
    if index1 == index2:
        return
    print("[", end="")
    for i in range(0, len(list)):
        if (i == index1 or i == index2):
            print('"' + str(list[i]) + '"', end="")
        else:
            print(list[i], end="")
        if (i != len(list) - 1):
            print(", ", end="")
        else:
            print("]")

def quicksort(list):
     
    def partition(list, low, high):
        global sum_comparisons
        global sum_swap
        pivot_index = (low + high) // 2
        pivot = list[pivot_index]  
        print_list(list, pivot_index, high)
        sum_comparisons += 1
        list[pivot_index], list[high] = list[high], list[pivot_index]
        sum_comparisons += 1
        sum_swap += 1
        i = low
        
        for j in range(low, high):
            if list[j] > pivot:
                print_list(list, i, j)  
                sum_comparisons += 1
                list[i], list[j] = list[j], list[i] 
                if i != j:
                    sum_swap += 1
                i += 1
        print_list(list, i, high) 
        sum_comparisons += 1
        list[i], list[high] = list[high], list[i]
        if i != j:
            sum_swap += 1

        return i
        
    def quicksort_helper(list, low, high):
        if low < high:
            pi = partition(list, low, high)
            quicksort_helper(list, low, pi - 1)
            quicksort_helper(list, pi + 1, high)
    
    quicksort_helper(list, 0, len(list) - 1)

listSize = (int)(input("ilość elementów tablicy: "))
listGen = (str)(input("czy liczby mają zostać wygenerowane losowo?(1 - tak, 0 - nie):  "))
list = []
while (listSize > 0):
    if (listGen == "1"):  
        c = randrange(-1000,1000)
    else:
        c = (int)(input("podaj liczbe: "))
    list.append(c)
    listSize -= 1

sum_comparisons = 0
sum_swap = 0
print(list)
startTime = datetime.datetime.now()    
quicksort(list)
endtime = datetime.datetime.now()
timeElapsed = endtime - startTime
seconds = timeElapsed.seconds
microsec = timeElapsed.microseconds
print(list)
print (f"{seconds} sekund , {microsec} milisekund")
print (f"Suma porownan: {sum_comparisons}")
print (f"Suma zamian: {sum_swap}")
