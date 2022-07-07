def countdown(num):
    count = []
    for x in range(num, 0, -1):
        count.append(x)
    return count
print(countdown(10))

def print_and_return(sum_list):
    print(sum_list[0])
    return sum_list[1]
print(print_and_return([1,2]))

def first_plus_length(sum_list):
    return sum_list[0] + len(sum_list)
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(sum_list):
    newlist = []
    for x in range(0, len(sum_list)):
        if sum_list[x] > sum_list[1]:
            newlist.append(sum_list[x])
    return newlist
print(values_greater_than_second([5,2,3,2,1,4, 8, 10]))

def length_value(num1, num2):
    newlist = []
    for x in range(0, num1):
        newlist.append(num2)
    return newlist
print(length_value(4,7))


