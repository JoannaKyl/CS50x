#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./Recover file\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    int image_count = 0;
    char filename[8] = {0};
    FILE *img = NULL;

    uint8_t buffer[512];

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {

            if (img != NULL)
            {
                fclose(img);
            }

            sprintf(filename, "%03i.jpg", image_count);
            image_count++;

            img = fopen(filename, "w");
        }

        if (img != NULL)
        {
            fwrite(buffer, 512, 1, img);
        }
    }

    if (img != NULL)
    {
        fclose(img);
    }
    fclose(card);
    return 0;
}
