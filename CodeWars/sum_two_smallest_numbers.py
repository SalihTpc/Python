def sum_two_smallest_numbers(numbers):
    # return sum(sorted(numbers)[:2]) # Mükemmel çözümlerden biri
    numbers.sort()
    a = numbers[0]
    b = numbers[1]
    # if a or b <= 0 and type(a) or type(b) == float:

    topla = a + b
    return topla
