import math


def get_credit():
    credit = 0
    while True:
        try:
            credit = int(input("Input Credit Card Number: "))
        except ValueError:
            print("Invalid Card Number.")
            continue
        else:
            break
    return credit


def check_digit():
    # credit = get_credit()
    sum = 0
    breakdown = 0
    for i in range(16):
        divisor = pow(10, i)
        digit = credit // divisor
        lastDigit = digit % 10
        multiplier = lastDigit * 2

        if i % 2 == 0:
            sum += lastDigit
        else:
            if multiplier <= 9:
                sum += multiplier
            else:
                breakdown = (multiplier % 10) + (multiplier // 10 % 10)
                sum += breakdown

    return sum


credit = get_credit()
sum = check_digit()
checkDigit = math. ceil(math.log10(credit))
first_digit = credit // pow(10, checkDigit - 1)
first_two_digit = credit // pow(10, checkDigit - 2)

if sum % 10 == 0:
    if checkDigit == 15 and (first_two_digit == 34 or first_two_digit == 37):
        print("AMEX")

    elif checkDigit == 16 and (first_two_digit == 51 or first_two_digit == 52 or first_two_digit == 53 or first_two_digit == 54 or first_two_digit == 55):
        print("MASTERCARD")

    elif first_digit == 4 and (checkDigit == 13 or checkDigit == 16):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
