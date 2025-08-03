import math
def median(input):
    my_list = sorted(input)
    n = len(input)
    mid = n // 2
    if n % 2 == 1:
        return my_list[mid]
    else:
        return (my_list[mid - 1] + my_list[mid]) / 2
my_list = [0, 1, 2, 3, 4, 5]
print(median([9, 1, 2, 3, 5, 7, 10]))
print(median(my_list))
