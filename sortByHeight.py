#skrypt sortuje liczby odatnie nie zmieniajac pozycji liczb ujemnych
#np z listy [-1,2,1,8,-1,10,5,-1] robi liste [-1,1,2,5,-1,8,10,-1]

def sortByHeight(a):
    z = 0
    old_list2 = []
    byheight = []

    old_list = sorted(a, key=int)
    for j in old_list:
        if j >= 0:
            old_list2.append(j)

    for i in a:
        if i < 0:
            byheight.append(i)
        elif i >= 0:
            byheight.append(old_list2[(z)])
            z += 1
    return byheight