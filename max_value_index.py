def find_max_value_index(num):
    max = 0
    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
            index = i
    return index

num = [1,6,9,8,5,2,4,10,3,56546,128,6,2,4,1]
print(find_max_value_index(num))