
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