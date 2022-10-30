"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
def count_digit_sum(number):
    integers = list(map(int, str(number)))
    sum_integers = sum(integers)

    return sum_integers

def main():
    number = 2 ** 1000
    sum_of_integers = count_digit_sum(number)

    print(sum_of_integers)

if __name__=="__main__": 
    main()    
