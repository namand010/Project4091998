

#######this alogo is working  with one sorted begining element and rest section is unsorted list, then comparing each elment of unsorted with the sorted elemnt
#####And Comparing if its greater left element with the next element in the list - swap or move to next element - this is more preferred w.r.t bubble and selection
def insertion_sort(list_a):
    indexing_length = range(1,len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i - 1] > value_to_sort and i > 0:
            list_a[i - 1],list_a[i] = list_a[i], list_a[i - 1]
            i -= 1
    return list_a


print(insertion_sort([10, 7, 8, 9, 1, 5]))
