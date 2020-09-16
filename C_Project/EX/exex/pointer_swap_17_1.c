#include <stdio.h>

//Q. 이대로 실행하면 메인 속 SwapIntPtr를 통한 결과값이 예상과는 다르게 뒤바뀌지 않을거야. 이유는?
void SwapIntPtr(int *p1, int *p2)
{
    int * temp = p1;
    p1 = p2;
    p2 = temp;
}

int main (void)
{
    int num1 = 10, num2 = 20;
    int *ptr1, *ptr2;
    
    ptr1 = &num1; ptr2 = &num2;
    printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);

    SwapIntPtr(ptr1, ptr2);
    printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);
    
    return 0;
}

//Answer.
/*
void SwapIntPtr(int **p1, int **p2)                     //2. 매개변수와 함수 내 변수 앞에 *을 하나씩 더 달아줌으로 인해 
{                                                             포인터 변수의 주소값을 가져올 수 있게 됨으로, 변경된 값을 
    int * temp = *p1;                                           저장할 수 있게 돼.
    *p1 = *p2;
    *p2 = temp;
}

int main (void)
{
    int num1 = 10, num2 = 20;
    int *ptr1, *ptr2;
    
    ptr1 = &num1; ptr2 = &num2;
    printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);

    SwapIntPtr(&ptr1, &ptr2);                           //1. &연산자를 붙여줘야 swap 함수의 값을 불러올거야.
    printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);         그렇지 않으면, 39번째 줄의 값을 그대로 받는 꼴이겠지.
    
    return 0;
}
*/
