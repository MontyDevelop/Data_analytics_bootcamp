import numpy as np


# arr1 = np.array([1,2,3,4])
# print(arr1)

# Output:
# [1 2 3 4]  (no commas) 

# list vs numpy arrays

# list sperate the data by coma and every can fit where they find the space
# But in numpy array data stick together and also fit together 



# l1 = [10,20,30]
# l2 = [40,50,60]

# print(l1+l2)

# a1 = np.array([10,20,30])
# a2 = np.array([40,50,60])

# print(a1 + a2)


# a3 = np.array([10,20,"30"])
# print(a3)

# Output:
# ['10' '20' '30']  All converted into string (because numpy only accept a single type of data)

# ------------------Metrices-----------------

# arr2 = np.array([[1,2,3,4],[5,6,7,8]]) # make sure equal number of item in every list
# print(arr2)

# Output:
# [[1 2 3 4]
#  [5 6 7 8]]

# ----------------------Slicing-----------------


# arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr2[0:2,0:2])

# Output:
# [[1 2]
#  [6 7]]


# arr2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr2[0:2,0:3]) # Beacuse numpy always work with equal items from each list

# Output:
# [[1 2 3]
#  [5 6 7]]

# print(arr2[0:2,0:2])
# Output:
# [[1 2]
#  [5 6]]


# print(arr2[0, 1:3])
# Output:
# [2 3]



# print(np.shape(arr2))
# Output:
# (2, 4) row = 2, columns = 4

# print(np.size(arr2)) # 8 total number of items

# -----------------Data conversion-------------

# arr2 = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr2.dtype)
# Output:
# int64


# arr3 = arr2.astype(float)
# print(arr3)

# Output:
# [[1. 2. 3. 4.]
#  [5. 6. 7. 8.]]


# -----------------------mathematical operations-----------------

# a1 = np.array([10,20,30])
# a2 = np.array([40,50,60])


# print(a1 + a2) # addition
# print(a1 - a2) # subtraction
# print(a1 * a2) # multiply
# print(a1 / a2) # divide

# print(np.add(a1, a2)) # addition
# print(np.subract(a1, a2)) # subtraction
# print(np.multiply(a1, a2)) # Multiply
# print(np.divide(a1, a2)) # Divide

# 2d arrays

# a1 = np.array([[10,20],[30,40]])
# a2 = np.array([[40,50],[60,70]])


# print(a1 + a2) # addition
# print(a1 - a2) # subtraction
# print(a1 * a2) # multiply
# print(a1 / a2) # divide

# print(np.add(a1, a2)) # addition
# print(np.subract(a1, a2)) # subtraction
# print(np.multiply(a1, a2)) # Multiply
# print(np.divide(a1, a2)) # Divide 


# arr1 = np.array([4,3,2,1])
# arr2 = np.array([2])

# print(np.power(arr1, arr2))

# Output:
# [16  9  4  1]


# arr1 = np.array([16,9,4,1])
# print(np.sqrt(arr1))

# Output:
# [4. 3. 2. 1.]  (in float use astype to make it int)




# -----------------Spliting and joining Arrays-----------------


# concatenate()

# a1 = np.array([10,20,30])
# a2 = np.array([40,50,60])

# print(np.concatenate([a1, a2]))
# Output:
# [10 20 30 40 50 60]


# print(np.concatenate([a1, a2], axis=0)) # we can't use axis = 1
# Output:
# [10 20 30 40 50 60] Because we have only one dimension in out arrays


# a1 = np.array([[10,20],[30,40]])
# a2 = np.array([[40,50],[60,70]])

# print(np.concatenate([a1, a2], axis=1)) #Horizontally

# Output:
# [[10 20 40 50]
#  [30 40 60 70]]

# print(np.concatenate([a1, a2], axis=0)) #Vertically

# Output:
# [[10 20]
#  [30 40]
#  [40 50]
#  [60 70]]


# np.hstack()
# np.vstack()

# a1 = np.array([10,20,30])

# print(np.array_split(a1, 2)) # here 2 is not the index it how many parts you want to make of this array. 

# Output:
# [array([10, 20]), array([30])]


# ------------------------Adding and removing --------------------------

a1 = np.array([10,20,30])


# np.append()
# print(np.append(a1, 90))

# Output:
# [10 20 30 90]


# np.insert()
# print(np.insert(a1, 2, 50))

# Output:
# [10 20 50 30]

# a1 = np.array([[10,20,30,40,50],[30,40,50,50,70]])

# print(np.insert(a1, 2, [90,90]))


# Output:
# [10 20 90 90 30 40 50 30 40 50 50 70]

# print(np.insert(a1, 2, [90,90], axis=1))


# Output:
# [[10 20 90 30 40 50]
#  [30 40 90 50 50 70]]


# a1 = np.array([[10,20,30,40,50],[30,40,50,50,70]])
# print(np.insert(a1, 1, [90,90], axis=0))
# Output:
# ValueError: could not broadcast input array from shape (1,2) into shape (1,5)


# a1 = np.array([[10,20],[30,40]]) # carefull about the shape
# print(np.insert(a1, 1, [90,90], axis=0))


# print(np.insert(a1, 1, [90], axis=0)) # It ll automatically take [90,90]

# Output:
# [[10 20]
#  [90 90]
#  [30 40]]


# print(np.insert(a1, [1,2], [90], axis=0))
# Output:
# [[10 20]
#  [90 90]
#  [30 40]
#  [90 90]]


# np.delete()
# a1 = np.array([[10,20],[30,40]])

# print(np.delete(a1, 1))

# Output:
# [10 30 40]

# print(np.delete(a1, 1, axis=0))
# Output:
# [[10 20]]


# print(np.delete(a1, 1, axis=1))
# Output:
# [[10]
#  [30]]


# -------------------------sort, filter, search----------------------



# arr1 = np.array([9,2,5,3,1,7])
# print(np.sort(arr1))
# Output:
# [1 2 3 5 7 9]

# arr1 = np.array([[9,2,5,3,1,7],[0,6,7,2,4,1]])
# print(np.sort(arr1))

# Output:
# [[1 2 3 5 7 9]
#  [0 1 2 4 6 7]]


# arr1 = np.array([9,2,5,3,1,7])
# b = np.where(arr1 == 5)
# print(b)


# Output:
# (array([2]),)  #2 is index


# arr1 = np.array([9,2,5,3,1,7,10, 8])
# b = np.where(arr1 % 2 == 0)
# print(b)

# Output:
# (array([1, 6, 7]),)


# searchsorted()

# arr1 = np.array([9,2,5,3,1,7,10,8])
# b = np.searchsorted(arr1, 3)
# print(b)

# Output:
# 5  (First it ll sort the array then search)
