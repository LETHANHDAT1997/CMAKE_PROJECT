# include_directories(Header_Inside1)

add_library(my_function_1
function_1.c)

target_include_directories(my_function_1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(my_function_1 PUBLIC ${CMAKE_SOURCE_DIR}/funtion_1/Header_Inside1)