

# DSA Practice day1 (Array) - "Find a mini value"

#def findmin(pArray)
Array = [1, 5, 10, 3, 2, 15]
Min = Array[0]

for i in Array:
    if i < Min:
       Min =  i

print('The min value is : ', Min)

    
