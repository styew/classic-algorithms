
def insertionSort(arry):
    for i in range(1,len(arry)):
        element = arry[i]
        j = i-1

        while j >=0 and element < arry[j]:
            arry[j+1] = arry[j]
            j -=1
        arry[j+1] = element

def bubbleSort(arry):
    lenght = len(arry)

    for i in range(lenght-1):
        for j in range(lenght-i-1):
            if arry[j+1] < arry[j]:
                arry[j+1],arry[j] = arry[j],arry[j+1]



arr1 = [12, 11, 13, 5, 6]
arr2 = [12, 11, 13, 5, 6]
bubbleSort(arr1)
insertionSort(arr2)
print(arr1,arr2)

