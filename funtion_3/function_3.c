#include"function_3.h"
#include "Header_Inside2_1.h"

int value_function_3_1=HEADER_MACRO_INSIDE2_1_VALUE_0,value_function_3_2=HEADER_MACRO_INSIDE2_1_VALUE_0,value_function_3_3=HEADER_MACRO_INSIDE2_1_VALUE_0;

int function_3_func1(int value1,int value2)
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


int function_3_func2(int value1,int value2)
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

int function_3_call(enum_function3 mode)
{
    static int return_value=0;
    switch (mode)
    {
    case enum_3_1:
        return_value=function_3_func1(value_function_3_1,value_function_3_2);
        break;
    case enum_3_2:
        return_value=function_3_func2(value_function_3_1,value_function_3_3);
        break;

    default:
        value_function_3_1=0;
        value_function_3_2=0;
        value_function_3_3=0;
        return_value=0;
        break;
    }
    return return_value;
}


int calculate(int value1,int value2)
{
    static int return_value=0;
    return_value=value1+value2;
    return return_value;
}