"""
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30
"""
def check_power(number):
    integers = list(map(int, str(number)))
    sum_integers = sum(integers)
    
    power = 1
    while True:
        result = pow(sum_integers, power)
     
        if result == number:
            print(f"{number} = {sum_integers} ** {power}")
            return True
        
        elif (result > number) or (result == 1):
            return False

        power += 1    

def main():
    power_numbers = []
    n = 0
    number = 10

    while True:
        
        result = check_power(number)
        if result == True:
            power_numbers.append(number)
            n += 1
            if n == 30:
                print(f"{n}th number is {number}")
                break

        number += 1

if __name__ == "__main__":
    main()
