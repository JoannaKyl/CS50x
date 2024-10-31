#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        return 1;
    }

    char *input = argv[1];
    int length = strlen(input);

    if (length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    for (int i = 0; i < length; i++)
    {
        if (!isalpha(input[i]))
        {
            return 1;
        }
    }

    // repeated characters? (upper/lower)
    for (int i = 0; i < length; i++)
    {
        char current = tolower(input[i]);
        for (int j = i + 1; j < length; j++)
        {
            char next = tolower(input[j]);
            if (current == next)
            {
                printf("Key has characters repeated\n");
                return 1;
            }
        }
    }

    string plaintext = get_string("plaintext:  ");

    int length1 = strlen(plaintext);
    printf("ciphertext: ");

    for (int i = 0; i < length1; i++)
    {
        if (isupper(plaintext[i]))
        {
            int number = plaintext[i] - 65;
            printf("%c", toupper(input[number]));
        }

        else if (islower(plaintext[i]))
        {
            int number1 = plaintext[i] - 65 - 32;
            printf("%c", tolower(input[number1]));
        }

        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}
