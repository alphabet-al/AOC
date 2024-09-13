def concat(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr[0]
    
    head = arr[0]
    tail = arr[1:]

    return head + concat(tail)

string = ['Hello', 'World']
print(concat(string))


