import numpy as np

meine_liste = [1,2,3]
print ("List: ",meine_liste)

# List to numpy array
np_vector = np.array(meine_liste)
print ("Numpy 1d Array: ",np_vector)

# creat Matrix
matrix = [[1,2,3],[4,5,6]]
print("Matrix: ",matrix)

# Matrix to numpy array 
np_array = np.array(matrix)
print ("Numpy 2d Array: \n", np_array)

# create array in a range 
array_range=np.arange(1,10)
print("Array in a Range: " ,array_range)

# array in range with 2 steps
array_range_step=np.arange(1,11,2)
print("Array in a Range with steps: " ,array_range_step)

# array with zeros
array_zero = np.zeros(5)
print("Array with zeros:", array_zero)

# multi zero array
array_zero_multi = np.zeros((5,5))
print("Multi Array with zeros: \n", array_zero_multi)

# array with ones 
array_ones = np.ones(3)
print("Array with ones:",array_ones)
array_ones_multi = np.ones((3,3))
print("Multi Array with ones: \n",array_ones_multi)

# array with equal split
array_easy_split=np.linspace(0,20,4)
print("Array with equal split from 0 to 20 with 4 values: \n", array_easy_split)
array_split=np.linspace(0,20)
print("Array with equal split from 0 to 20 with 50 values: \n", array_split)

# identity matrix/array ( ger.: Einheitsmatrix)
identity_array= np.eye(5)
print("Identity matrix: \n", identity_array)

# radom array from 0-1 (ger.: Zufallsmatrix)
random_array= np.random.rand(2)
print("Random array:  ",random_array)

# radom array with int 
random_int_array= np.random.randint(1,100,10)
print("Random array with int values: ", random_int_array)


arr = np.arange(25)
ranarr=np.random.randint(0,50,10)

# resahp array 
new_arr=arr.reshape(5,5)
print(arr)
print(new_arr)

# maximum value and position in the array 
max_value= ranarr.max()
print(max_value)
position_max_value=ranarr.argmax()
print(position_max_value)

# minimum value and position in the array 
min_value = ranarr.min()
print(min_value)
position_min_value= ranarr.argmin()
print(position_min_value)

# get the dimension of the array 
print(arr.shape)
print(ranarr.shape)

# get the data typ of the array
print(arr.dtype) 