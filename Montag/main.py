from random import randint
import time
#array[0-99][1-100]

def befülle_liste():
    outputListe = []
    for i in range(0,1000):
        outputListe.append(randint(1,100))
    return outputListe

def algo():
    arr1 = befülle_liste()
    arr2 = befülle_liste()
    arr3 = befülle_liste()
    startTime = time.time()
    #hier kann der Aglorithmus hin
    arr = arr1+arr2+arr3
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    endTime = time.time() - startTime 
    print(arr)
    print(endTime)



algo()