#include "stdio.h"
#include "function_1.h"
#include "function_2.h"
#include "function_3.h"
#include "Header_1.h"
#include "Header_2.h"
#include "Header_3.h"
#include "funtion_1/Header_Inside1/Header_Inside1_1.h"
#include "funtion_1/Header_Inside1/Header_Inside1_2.h"

int value1=HEADER_MACRO_INSIDE1_1_VALUE_1, value2=HEADER_MACRO_INSIDE1_2_VALUE_1;

int main()
{   
    static int return_value=0;

    printf("\n************************************************** CMakeFiles Test ****************************************************");

    switch (return_value)
    {
        case 0:
            return_value=function_1_func1( value1, value2);
            break;
        case 1:
            return_value=function_2_func1( value1, value2);
            break;   
        case 2:
            return_value=function_3_func1( value1, value2);
            break;         
        default:
            return_value=0;
            value1=0;
            value2=0;
            calculate(10,5);
            break;
    }
    
    printf("\n******************************************************** END ****************************************************");
    return return_value;
}