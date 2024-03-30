#include"function_2.h"
#include "Header_1.h"
int value_function_2_1=HEADER_1_MACRO_1,value_function_2_2=HEADER_1_MACRO_1,value_function_2_3=HEADER_1_MACRO_1;

int function_2_func1(int value1,int value2)
{
    static int return_value=0;
    if (value1 > value2)
    {
        return_value=value1-value2;
    }else
    {
        return_value=value2-value1;
    }

    return return_value;
}


int function_2_func2(int value1,int value2)
{
    static int return_value=0;
    if (value2 != 0) 
    {
        return_value=value1/value2;
    }else if(value1 !=0)
    {
        return_value=value2/value1;
    }

    return return_value;
}

int function_2_call(enum_function2 mode)
{
    static int return_value=0;
    switch (mode)
    {
    case enum_2_1:
        return_value=function_2_func1(value_function_2_1,value_function_2_2);
        break;
    case enum_2_2:
        return_value=function_2_func2(value_function_2_1,value_function_2_3);
        break;

    default:
        value_function_2_1=0;
        value_function_2_2=0;
        value_function_2_3=0;
        return_value=0;
        break;
    }
    return return_value;
}