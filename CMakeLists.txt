# The following five lines of boilerplate have to be in your project's
# CMakeLists in this exact order for cmake to work correctly
cmake_minimum_required(VERSION 3.16)

set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -g")
set(CMAKE_BUILD_TYPE Debug) #Phai co dong nay moi debug GDB bang lenh layout src duoc

include_directories(Lib_funtion)

add_subdirectory(funtion_1)
add_subdirectory(funtion_2)
add_subdirectory(funtion_3)

add_executable(main main.c)

target_link_libraries(main PUBLIC my_function_1 my_function_2 my_function_3)

#cmake -S . -B ./build -G "MinGW Makefiles"
#mingw32-make -C build