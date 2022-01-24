
def maxAndminiteger(list):
    max = min = list[0]
    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

print(maxAndminiteger([1,2,3,0,9,10,-1]))

# def findelem(array):
#     new_array = array
#     count = 0
#     for i in array:
#         if i in new_array:
#             count+= 1
#     return i
#
# print(findelem([12,3,3,5,6]))



#
#     count = 0
#     new_array = []
#     for i in array:
#         if i in new_array:
#             count+= 1
#             new_array.append(count[i])
#
#     for j in new_array:
#         if j != count[1]:
#     return j
#
#
#
#
#
#
# {1:1, 2:2, 3:3, 5:1, 6:1}
# [1, 2, 2, 3,3,3, 5, 6]
#
