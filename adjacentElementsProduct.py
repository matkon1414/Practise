#skrypt oblicza najwiekszy iloczyn podanych liczb z listy

def adjacentElementsProduct(inputArray):
    new_list=[]
    n = 0
    for number in inputArray:
        if n < len(inputArray)-1:
            new_list.append(number*inputArray[n+1])
        n +=1

    return max(new_list)