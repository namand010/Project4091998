
"""
This is log2n -----Big 0 - in every step lists get half.
"""
def binary_earch(seq_a, item):
    begin_index = 0
    end_index = len(seq_a)
    while begin_index <= end_index:
        mid_point = begin_index + (end_index - begin_index) // 2 # Rest of the elements at the right
        mid_point_value = seq_a[mid_point]

        if mid_point_value == item:
            return mid_point
        elif item < mid_point_value:     #####compare mid with item is less mid then change the last_index -1
            end_index = mid_point - 1
        else:
            begin_index = mid_point + 1 #####compare mid with item is greater then change the begin_index -1
    return None

a = [1,2,3,4,5,6]
print(binary_earch(a,6))