def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        maxid = 0
        for j in range(1, i+1):
            if alist[j] > alist[maxid]:
                maxid = j
        alist[maxid], alist[i]=alist[i], alist[maxid]
    

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)