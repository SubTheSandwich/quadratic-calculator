import math
from fractions import Fraction

a = int(input("A?"))
b = int(input("B?"))
c = int(input("C?"))
ask = input("Convert to fraction? (True/False)")
ask2 = input("Round to nearest hundreth? (TRUE/FALSE)")


p1 = -1 * b + math.sqrt(b ** 2 - 4 * a * c)
p2 = -1 * b - math.sqrt(b ** 2 - 4 * a * c)
newA = 2 * a
solution1 = p1 / newA
solution2 = p2 / newA
rounded = round(solution1, 2)
rounded2 = round(solution2, 2)

def main():
    if ask == "TRUE":
        if ask2 == "TRUE":
            print("x = {" + str(rounded) + ", " + str(rounded2) + "}")
        else:
            print("x = {" + str(Fraction(solution1)) + ", " + str(Fraction(solution2)) + "}")
    else:
        if ask2 == "TRUE":
            print("x = {" + str(rounded) + ", " + str(rounded2) + "}")
        else:
            print("x = {" + str(solution1) + ", " + str(solution2) + "}")

if __name__ == "__main__":
    main()