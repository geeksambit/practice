#include <stdio.h>

int main()
{
    int i, j;
    int matrix[10][20];

    
    int m = 5; //number of row 
    int n = 10; // number of colomn 
    int start =15 ; // start point of number
    int diff = 20 ; // difference betwn two consecutive number 

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            matrix[i][j]=start;
            if (j==n-1){
                start = 15;
            }
            else{
                start = start + diff;
            }
            
        }
    }

    /* Display the matrix */
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}

