def insertion_sort(a):
    for i in range(1, len(a)):
        j = i-1
        while a[j] > a[j+1] and j >= 0:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
