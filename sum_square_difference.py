"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def squares_sum_difference(numbers):

    sum_of_squares = 0
    
    for number in numbers:
        sum_of_squares += number ** 2

    square_of_sum = sum(numbers) ** 2

    difference = square_of_sum - sum_of_squares

    return difference


def main():
    numbers = list(range(1, 101))
    diff = squares_sum_difference(numbers)

    print(diff)
    

if __name__ == "__main__":
    main()
