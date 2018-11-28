#skrypt pokazuje czy liczba o parzystej ilosci liczb np 12,1245,0987
#jest szczesliwa(tzn suma lewej strony tej liczny i prawej sa rowne)

def isLucky(n):
    L= []
    idk = str(n)
    x = list(idk)
    howlong = len(x)//2
    for item in x:
        L.append(int(item))
    if sum(L[:howlong]) == sum(L[howlong:]):
        return True
    else:
        return False