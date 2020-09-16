#include <stdio.h>

int Add (int n1, int n2)
{
    return n1 + n2;
}

int main (void)
{
    int result;
    result = Add(3, 4);
    printf("add result1 : %d\n" , result);

    result = Add(5, 8);
    printf("add result2 : %d\n", result);

    return 0;
}
//함수 정의하기 