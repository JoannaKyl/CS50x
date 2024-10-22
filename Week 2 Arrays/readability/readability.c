#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main()
{
    string text = get_string("Text:");
    int length = strlen(text);
    int spaces = 0;

    int sentecens = 0;
    int letters = 0;

    // printf ("%d",text[3]);

    // claculate spaces
    for (int i = 0; i <= length; i++)
    {
        if (text[i] == 32)
        {
            spaces += 1;
        }
    }
    // calculate letters
    for (int i = 0; i < length; i++)
    {
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
        {
            letters += 1;
        }
    }

    // calculate sentences
    for (int i = 0; i < length; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentecens += 1;
        }
    }

    int words = spaces + 1;
    // calculate Coleman-Liau Index
    double L = (double) letters / words * 100;
    double S = (double) sentecens / words * 100;
    double index = (0.0588 * L) - (0.296 * S) - 15.8;

    if (index == 16 || index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else
        printf("Grade %.0f\n", round(index));

    printf("words:%d ,letters:%d ,spaces:%d,sentence:%d ",words ,letters,spaces,sentecens);

}
