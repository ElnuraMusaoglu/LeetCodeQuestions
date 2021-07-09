'''
Find the missing number in the array
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x.
You have to find x.
The input array is not sorted. Look at the below array and give it a try before checking the solution.
'''

def find_missing(input):
    total = 0
    max = 0
    for i in range(len(input)):
        total += input[i]
        max = input[i] if input[i] > max else max

    total_real = max * (max+1) / 2
    return int(total_real - total)


def find_missing2(input):
    sum_of_elements = sum(input)
    max = len(input) + 1
    actual_sum = (max * (max + 1)) / 2
    return actual_sum - sum_of_elements

result = find_missing([2,3,4,5,9,8,7,1])
print(result)


def find_sum_of_two(A, val):
 #TODO: Write - Your - Code
  return

