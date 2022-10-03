def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0]+numbers[1]


numbers = [19, 5, 42, 2, 77]

print(sum_two_smallest_numbers(numbers))
