list1 = [1, 2, 3, 5]
list2 = [11, 22, 33, 55]


# first approach 
def item_in_common(ls1, ls2):
    for i in ls1:
        for j in ls2:
            if i == j:
                return i
    return False


# second approach 
def item_in_common_better(ls1, ls2):
    dict1 = {}
    for i in ls1:
        dict1[i] = True
    for j in ls2:
        if j in dict1:
            return j
    return False



result = item_in_common(list1, list2)
print(result)


result1 = item_in_common_better(list1, list2)

print(result1)

