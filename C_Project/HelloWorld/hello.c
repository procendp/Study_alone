#include <stdio.h>

int main(void)
{
    //return 0;
    printf("Hello, World!\n");
     //return 0; 이 위치까지만 보여지고 main 함수 종료됨
    printf("HI, C!\n 1\n 2\n 3\n 4\n" );
    printf("GoodBye\n");
    //3+4; 컴파일 ㅇㅋ, 실행 ㅇㅋ, 하지만 나타나진 않음.
    printf("%d %d \n", 12, 14.555);
    ////////////////////////////////////////////////////////////////////////////

    int num;
    num = 3+4;
    printf("%d \n", num); //결과는 7이 나옴...
    
    /*int num 하고 문장 실행하는 순간 정수 저장 공간이 할당되고(int)
      그 할당 공간의 이름은 num으로 붙는다.(num)
      그리고, 그 num에 3+4가 계산된 값이 저장되고
      printf를 통해 계산 값인 '7'이 출력된다.
    */

    return 0; 
}
