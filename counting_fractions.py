from fractions import Fraction

def create_fractions(number):
    fractions = []

    counter = 1
    divider = 1
    while counter < number + 1:
        while divider < number + 1:
            if counter % divider == 0:
                divider += 1
                continue
            
            elif counter >= divider:
                divider += 1 
                continue    

            fraction = Fraction(counter, divider)
            if fraction not in fractions:
                fractions.append(fraction)    
                
            divider += 1


        divider = 1
        counter += 1      
    
    sorted_fractions = sorted(fractions)
    print(sorted_fractions)
    print(len(sorted_fractions))


def main():
    number = 8
    create_fractions(number)


if __name__ == "__main__":
    main()
