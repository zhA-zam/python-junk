from copy import deepcopy

alist = [[1,2,3],[4,5,6]]
blist = alist
alist[0][0] = 0
print(alist == blist)
print(alist is blist)

clist = deepcopy(alist)
print(alist == clist)
print(alist is clist)
