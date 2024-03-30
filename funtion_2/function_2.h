#ifndef _FUNCTION_2_H_
#define _FUNCTION_2_H_
typedef enum _enum_function2_
{
    enum_2_0=0,
    enum_2_1=1,
    enum_2_2=2,
}enum_function2;

int function_2_func1(int value1,int value2);
int function_2_func2(int value1,int value2);
int function_2_call(enum_function2 mode);




#endif
