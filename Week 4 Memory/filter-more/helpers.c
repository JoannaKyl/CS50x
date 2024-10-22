#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int modified_colour =
                round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = modified_colour;
            image[i][j].rgbtGreen = modified_colour;
            image[i][j].rgbtRed = modified_colour;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            RGBTRIPLE tempstore = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tempstore;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image_copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            double sumBlue = 0;
            double sumRed = 0;
            double sumGreen = 0;

            int startRow = (i - 1 < 0) ? 0 : i - 1;
            int endRow = (i + 1 > height - 1) ? height - 1 : i + 1;
            int startColumn = (j - 1 < 0) ? 0 : j - 1;
            int endColumn = (j + 1 > width - 1) ? width - 1 : j + 1;

            for (int k = startRow; k <= endRow; k++)
            {
                for (int l = startColumn; l <= endColumn; l++)
                {
                    sumRed += image_copy[k][l].rgbtRed;
                    sumGreen += image_copy[k][l].rgbtGreen;
                    sumBlue += image_copy[k][l].rgbtBlue;
                    count++;
                }
            }
            int avgRed = round(sumRed / count);
            int avgGreen = round(sumGreen / count);
            int avgBlue = round(sumBlue / count);
            image[i][j].rgbtRed = avgRed;
            image[i][j].rgbtGreen = avgGreen;
            image[i][j].rgbtBlue = avgBlue;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    RGBTRIPLE image_copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image_copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gxRedSum = 0;
            int gxGreenSum = 0;
            int gxBlueSum = 0;
            int gyRedSum = 0;
            int gyGreenSum = 0;
            int gyBlueSum = 0;

            for (int m = i - 1; m <= i + 1; m++)
            {
                for (int n = j - 1; n <= j + 1; n++)
                {
                    if (m < 0 || m > height - 1 || n < 0 || n > width - 1)
                    {
                        continue;
                    }
                    else if (m == i - 1 && n == j - 1)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[0][0];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[0][0];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[0][0];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[0][0];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[0][0];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[0][0];
                    }
                    else if (m == i - 1 && n == j)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[0][1];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[0][1];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[0][1];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[0][1];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[0][1];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[0][1];
                    }
                    else if (m == i - 1 && n == j + 1)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[0][2];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[0][2];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[0][2];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[0][2];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[0][2];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[0][2];
                    }
                    else if (m == i && n == j - 1)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[1][0];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[1][0];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[1][0];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[1][0];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[1][0];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[1][0];
                    }
                    else if (m == i && n == j)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[1][1];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[1][1];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[1][1];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[1][1];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[1][1];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[1][1];
                    }
                    else if (m == i && n == j + 1)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[1][2];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[1][2];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[1][2];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[1][2];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[1][2];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[1][2];
                    }
                    else if (m == i + 1 && n == j - 1)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[2][0];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[2][0];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[2][0];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[2][0];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[2][0];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[2][0];
                    }
                    else if (m == i + 1 && n == j)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[2][1];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[2][1];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[2][1];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[2][1];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[2][1];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[2][1];
                    }
                    else if (m == i + 1 && n == j + 1)
                    {
                        gxRedSum += image_copy[m][n].rgbtRed * Gx[2][2];
                        gxGreenSum += image_copy[m][n].rgbtGreen * Gx[2][2];
                        gxBlueSum += image_copy[m][n].rgbtBlue * Gx[2][2];
                        gyRedSum += image_copy[m][n].rgbtRed * Gy[2][2];
                        gyGreenSum += image_copy[m][n].rgbtGreen * Gy[2][2];
                        gyBlueSum += image_copy[m][n].rgbtBlue * Gy[2][2];
                    }
                    else
                    {
                        continue;
                    }
                }
            }
            int redResult = round(sqrt(pow(gxRedSum, 2) + pow(gyRedSum, 2)));
            int greenResult = round(sqrt(pow(gxGreenSum, 2) + pow(gyGreenSum, 2)));
            int blueResult = round(sqrt(pow(gxBlueSum, 2) + pow(gyBlueSum, 2)));
            image[i][j].rgbtRed = fmin(redResult, 255);
            image[i][j].rgbtGreen = fmin(greenResult, 255);
            image[i][j].rgbtBlue = fmin(blueResult, 255);
        }
    }
    return;
}
