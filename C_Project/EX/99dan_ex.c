#include <stdio.h>
int main(void)
{
    int cur = 2, is = 0;
    while (cur < 10)
    {
        //밑에 is = 1 을 넣고, 위에 is = 1이 아닌 is = 0으로 하는 게 뭐가 다를까.
        is = 1;
        while (is < 10)
        {
            printf("%d x %d = %d\n", cur, is, cur*is);
            is++;
        }
        cur++;
    }
    return 0;
}