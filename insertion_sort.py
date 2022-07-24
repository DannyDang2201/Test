def insertion_sort(a):
    for i in range(1, len(a)):
        cur_val = a[i]
        j = i - 1
        while j >= 0 and cur_val < a[i]:
            a[j+1] = a[j]
            j -= 1


A = [1, 3, 5, 124, 0, -223, 44, 146]
insertion_sort(A)
print(A)
