#include <iostream>

int main()
{
    int a;
    0 <= a <= 100;
    std::cin >> a;

    if (a >= 90 && a <= 100)
    {
        std::cout << "A" ;
    }
    else if (a >= 80 && a <= 89)
    {
        std::cout << "B" ;
    }
    else if (a >= 70 && a <= 79)
    {
        std::cout << "C" ;
    }
    else if (a >= 60 && a <= 69)
    {
        std::cout << "D" ;
    }
    else
    {
        std::cout << "F" ;
    }

    return 0;
}