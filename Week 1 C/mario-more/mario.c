#include <cs50.h>
#include <stdio.h>

int main()
{

    int height;

    do
    {
        height = get_int("Height:");
    }
    while (height < 1 || height > 8);

    for (int i = 1; i <= height; i++)
    {

        for (int j = 1; j <= height - i; j++)
        {
            printf(" ");
        }

        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }

        printf("  ");

        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}
