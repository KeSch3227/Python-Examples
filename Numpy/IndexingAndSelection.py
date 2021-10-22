import numpy as np

# Indexing 
arr = np.arange(0,11)
print(arr)

# define one value of the array 
print(arr[8])

# define start and stop  
print(arr[1:5])

#set new value for the range 
arr[0:5] =100
print(arr)

arr = np.arange(0,11)
print(arr)

# not copy only refrenz 
teil_arr= arr[0:6]
print(teil_arr)
teil_arr[:]=99
print(teil_arr)
print(arr)

# create copy
arr_kopie = arr.copy()
print(arr_kopie)

# indexing with more dimension 
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
print(arr_2d[1])
print(arr_2d[1,0])
print(arr_2d[:2,1:])


#Selection
arr = np.arange(1,11)
bool_arr = arr>5
print(bool_arr)
print(arr[bool_arr])



