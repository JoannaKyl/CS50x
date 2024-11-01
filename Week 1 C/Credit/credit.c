#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main()
{
    long cr = get_long("Number: ");
    int checkDigit = (log10(cr) + 1);
    int sum = 0;
    for (int i = 0; i <= 15; i++)
    {
        long divisor = pow(10, (i));
        long digit = cr / divisor;
        long lastDigit = digit % 10;
        long multiplier = lastDigit * 2;

        if (i % 2 == 0)
        {
            sum += lastDigit;
        }
        else
        {
            if (multiplier <= 9)
            {
                sum += multiplier;
            }
            else
            {
                long breakdown = (multiplier % 10) + (multiplier / 10 % 10);
                sum += breakdown;
            }
        }
    }
    long first_digit = cr / pow(10, checkDigit - 1);
    long first_two_digit = cr / pow(10, checkDigit - 2);
    // check card details
    if (sum % 10 == 0)
    {
        if (checkDigit == 15 && (first_two_digit == 34 || first_two_digit == 37))
        {
            printf("AMEX\n");
        }
        else if (checkDigit == 16 &&
                 (first_two_digit == 51 || first_two_digit == 52 || first_two_digit == 53 ||
                  first_two_digit == 54 || first_two_digit == 55))
        {
            printf("MASTERCARD\n");
        }
        else if ((checkDigit == 13 || checkDigit == 16) && first_digit == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
