//왜 안 되지, 다시 해봐
#include <stdio.h>

int main(void){
    
    int n1 = 1, n2 = 0;
    while (n1 < 3) //n1 = 0 1 2
    {
        n2 = 1;
        while (n2 < 4) //n2 = 0 1 2 3
        {
            printf("%d %d \n", n1, n2);
            n2++;
        }

        //printf("%d %d \n",  n1, n2);
        n1++;
    
    }
       return 0;
}