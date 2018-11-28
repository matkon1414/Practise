#skrypt pokazuje liste nadluzszych stringow z podanej listy

def allLongestStrings(array):
    k = []
    for item in array:
        if len(item) == len(max(array, key = len)):
            k.append(item)
    return k