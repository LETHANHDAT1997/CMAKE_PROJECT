add_library(my_function_2
function_2.c)

target_include_directories(my_function_2 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})