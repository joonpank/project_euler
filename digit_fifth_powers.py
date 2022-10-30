"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def calculate_sum_power_n(number, power):
    integers = list(map(int, str(number)))
    fifth_power_elements = [pow(x, power) for x in integers]
    total_sum = sum(fifth_power_elements)

    return total_sum


def main(power):
    number = pow(10, power - 1)
    numbers = []
    while number < pow(10, power):
        if number == calculate_sum_power_n(number, power):
            print(number)
            numbers.append(number)

        number += 1

    sum_of_numbers = sum(numbers)
    print(f"Sum of {power}-digit numbers is: {sum_of_numbers}")


if __name__ == "__main__":
    main(power = 5)