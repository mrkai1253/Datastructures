# print(len(lst))


def insertion_sort(lst):
    for _ in range(len(lst)):
        for i in range(1,len(lst)):
            if lst[i] < lst[i - 1]:
                t = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = t
                print(lst)

    return lst


l = insertion_sort([5, 2, 4, 6, 1, 3])

print(l)
