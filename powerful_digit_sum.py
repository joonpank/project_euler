"""
Project Euler problem 56.

'A googol (10100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

def main():
    sums = []

    a = 1
    b = 1

    while a < 100:
        while b < 100:
            power = pow(a, b)
            integers = list(map(int, str(power)))
            sum_integers = sum(integers)

            sums.append(sum_integers)

            b += 1

        b = 1
        a += 1

    print(max(sums))

if __name__ == "__main__":
    main()