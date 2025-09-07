def modify(list1):
    list1[0]=0
    list1[1]=1
    list1[2]=2
    list1[3]=3

def main():
    lista=[1,2,3,4]
    print("Before modification:",lista)
    modify(lista)
    print("After modification and no return:",lista)
    print(lista)

main()