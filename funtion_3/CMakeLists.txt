# include_directories(${CMAKE_SOURCE_DIR}/funtion_2/Header_Inside2)

add_library(my_function_3
function_3.c)

target_include_directories(my_function_3 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(my_function_3 PUBLIC ${CMAKE_SOURCE_DIR}/funtion_2/Header_Inside2)