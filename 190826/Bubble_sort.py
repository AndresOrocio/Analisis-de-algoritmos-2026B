import time 

def bubble_sort(arr):
    # complejidad temporal
    #print (len(arr))

    #time.sleep(100)

    n = len(arr) # 0(1)

    #bucle exterior:

    for i in range(n): # 0(n)
        #Bucle interior:

        for j in range(0, n -1 - 1): # 0(n)

            # comparacion: 0(1)
            if arr[j] > arr[j + 1]: # 0(1)
                #Intercambio: 0(1)
                 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # 0(1)

array = [6,5,3,1,8,7,2,4] # 0(1)

bubble_sort(array) #0(n a la 2)
  
print("\n")   # 0(1)
print("lista ordenada", array, "\n")  # 0(n)
print("------------------------------------------")  # 0(1)

