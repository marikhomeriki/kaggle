def fizz_buzz(num):
    result = [i+1 for i in range(num)]

    for i in result:

        if i % 3 == 0 and i % 5 > 0:
            result[i-1] = 'Fizz'
        elif i % 5 == 0 and i % 3 > 0:
            result[i-1] = 'Buzz'
        elif i % 3 == 0 and i % 5 == 0:
            result[i-1] = 'FizzBuzz'

    return result


num = 20

print(fizz_buzz(num))

x = fizz_buzz(num)
test = x.count('Fizz')
print(test)
