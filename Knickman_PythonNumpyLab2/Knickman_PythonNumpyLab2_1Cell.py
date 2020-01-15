#Andrew Knickman
#ITEC 345
#Python Numpy lab 2


import numpy as np
arr_rand = np.array([8, 8, 3, 7, 7, 0, 4, 2, 5, 2])
print("Array: ", arr_rand)

index_gt5 = np.where(arr_rand > 5)
print("Positions where value > 5:",index_gt5)

arr_rand.take(index_gt5)
np.where(arr_rand>5,'gt5','le5')

print("Position of max value:",np.argmax(arr_rand))
print("Position of min value:",np.argmin(arr_rand))

path = "NumpyLab2DS.txt"
data = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=None, encoding=None)
data[:3]


#np.savetxt("out.csv",data,delimiter=",")

np.save('myarray.npy',arr_rand)
arr_rand2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
np.savez('array.npz',arr_rand,arr_rand2)

a = np.load('myarray.npy')
print(a)

b = np.load('array.npz')
print(b.files)
b['arr_0']

a = np.zeros([4,4])
b = np.ones([4,4])
print(a)
print(b)

np.concatenate([a,b],axis=1)
np.hstack([a,b])
np.c_[a,b]

np.r_[[1,2,3],0,0,[4,5,6]]

arr = np.random.randint(1,6,size=[8,4])
arr

np.sort(arr,axis=0)

x = np.array([1, 10, 5, 2, 8, 9])
sort_index = np.argsort(x)
print(sort_index)

x[sort_index]

sorted_index_1stcol = arr[:,0].argsort()
arr[sorted_index_1stcol]

arr[sorted_index_1stcol[::-1]]

lexsorted_index = np.lexsort((arr[:,1],arr[:,0]))
arr[lexsorted_index]