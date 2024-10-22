#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

    string player1 = get_string("Player 1:");
    string player2 = get_string("Player 2:");
    int length1 = strlen(player1);
    int length2 = strlen(player2);
    int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int score = 0;
    int score1 = 0;
    int score2 = 0;

    for (int i = 0; i <= length1; i++)
    {
        if (player1[i] >= 65 && player1[i] <= 90)
        {
            score = points[(player1[i] - 65)];
            score1 += score;
        }
        else if (player1[i] >= 97 && player1[i] <= 122)
        {
            score = points[(player1[i] - 32 - 65)];
            score1 += score;
        }
    }

    for (int i = 0; i <= length2; i++)
    {
        if (player2[i] >= 65 && player2[i] <= 90)
        {
            score = points[(player2[i] - 65)];
            score2 += score;
        }
        else if (player2[i] >= 97 && player2[i] <= 122)
        {
            score = points[(player2[i] - 32 - 65)];
            score2 += score;
        }
    }

    if (score1 == score2)
    {
        printf("Tie!\n");
    }

    else if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }
}
