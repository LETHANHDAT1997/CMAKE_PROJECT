#ifndef _FUNCTION_3_H_
#define _FUNCTION_3_H_
typedef enum _enum_function3_
{
    enum_3_0=0,
    enum_3_1=1,
    enum_3_2=2,
}enum_function3;

int function_3_func1(int value1,int value2);
int function_3_func2(int value1,int value2);
int function_3_call(enum_function3 mode);




#endif
