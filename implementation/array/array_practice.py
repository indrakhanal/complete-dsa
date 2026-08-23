from array import *
import numpy as np

# Add items from list into array using fromlist() method
# templist = [1, 2, 3, 4, 500]
# arr = array('i', [1, 2, 3, 4, 5])
# arr.fromlist(templist)
# print(arr.index(500))  # Get index of element
# print(arr)

# numdays = input("How many day's temperature?")
# temparr = []
# sumtemp = 0
# for i in range(int(numdays)):
#     temp = input("Enter the temperature for day " + str(i + 1) + ": ")
#     temparr.append(int(temp))
#     sumtemp += int(temp)

# avgtemp = sumtemp / int(numdays)

# print("Average temperature is: " + str(avgtemp))

# sum_above_avg = 0
# for i in temparr:
#     if i > avgtemp:
#         sum_above_avg += 1
# print("Number of days with temperature above average: " + str(sum_above_avg))


def missing_number(arr, n):
    # TODO
    # total_sum = n * (n+1) // 2
    # array_sum = sum(arr)
    # missing_number =  total_sum-array_sum
    # return missing_number
    missing_number_list = []
    actual_arr = [i for i in range(1, n + 1)]
    for i in actual_arr:
        if i not in arr:
            missing_number_list.append(i)
    return missing_number_list


# check if number is present or not in python array
def check_number_presence(array_, number):
    for i in range(len(array_)):
        if array_[i] == number:
            return i



# Find the maximum product of two integers in an array where all elements are positive.
# Example
# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)

#Method 1
def max_product(arr):
    largest_num = 0
    for i in range(len(arr)):   #O(n) time complexity
        for j in range(i+1, len(arr)):   #O(n2) time complexity
            product = arr[i]*arr[j]
            if product < largest_num:
                continue
            largest_num = product
    return largest_num

# form method 1 we have O(n2) time complexity with O(1) space complexity, so this is not a optimal solution

#Method2
#Method 2 only have O(n) time complexity so it is the optimal solution for this problem
def max_product_optimal(arr):
    max1, max2 = 0, 0
    for num in arr: #O(n) time 
        if max1 < num:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return max1*max2
            
    
array_ = np.array([1,2,3,4,5,6,7,8,9,10])   
print(max_product(array_)) 
# print(missing_number([1, 6], 6))


#Contains dUPLICATES

def contains_duplicates(nums):
    seen  = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

print(contains_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))


