
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