def spacey(array):
    arr = ''
    for i in range(len(array)):
        array[i] = arr + array[i]
        arr = array[i]
    return array


array = ['kevin', 'has', 'no', 'space']

print(spacey(array))
