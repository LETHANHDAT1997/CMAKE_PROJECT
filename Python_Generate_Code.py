# import openpyxl

# def read_excel_columns(file_path, sheet_name):
#     """
#     Đọc hai cột A và B từ file Excel cho đến khi cả hai ô đều rỗng.

#     Args:
#     - file_path (str): Đường dẫn tới file Excel.
#     - sheet_name (str): Tên của sheet trong file Excel.

#     Returns:
#     - list: Danh sách các cặp giá trị từ cột A và B.
#     """
#     try:
#         workbook = openpyxl.load_workbook(file_path)
#         sheet = workbook[sheet_name]

#         data = []
#         row = 1
#         while True:
#             value_A = sheet.cell(row=row, column=1).value
#             value_B = sheet.cell(row=row, column=2).value
#             if value_A is None and value_B is None:
#                 break
#             data.append((value_A, value_B))
#             row += 1

#         workbook.close()
#         return data
#     except Exception as e:
#         print("Đã xảy ra lỗi:", e)
#         return None

# if __name__ == "__main__":
#     excel_file_path = "example.xlsx"  # Đường dẫn tới file Excel
#     excel_sheet_name = "Sheet1"       # Tên của sheet trong file Excel

#     # Đọc hai cột từ file Excel
#     column_data = read_excel_columns(excel_file_path, excel_sheet_name)

#     if column_data is not None:
#         print("Dữ liệu từ cột A và B:")
#         for item1,item2 in column_data:
#             print(item1)
#             print(item2)
#     else:
#         print("Có lỗi xảy ra khi đọc file Excel.")

###############################################################################################################################

# def write_to_c_file(string, file_path):
#     """
#     Ghi chuỗi vào file .c.

#     Args:
#     - string (str): Chuỗi cần ghi vào file.
#     - file_path (str): Đường dẫn tới file .c.
#     """
#     with open(file_path, 'w') as f:
#         f.write(f'#include <stdio.h>\n\n')
#         f.write(f'int main() {{\n')
#         f.write(f'\tprintf("{string}");\n')
#         f.write(f'\treturn 0;\n')
#         f.write(f'}}\n')

###############################################################################################################################

# def write_to_c_file(strings, file_path):
#     """
#     Ghi tất cả các chuỗi từ một danh sách vào file .c.

#     Args:
#     - strings (list): Danh sách các chuỗi cần ghi vào file.
#     - file_path (str): Đường dẫn tới file .c.
#     """
#     try:
#         with open(file_path, 'w') as f:
#             f.write('#include <stdio.h>\n\n')
#             f.write('int main() {\n')
#             for string in strings:
#                 f.write('\tprintf("%s\\n");\n' % string)
#             f.write('\treturn 0;\n')
#             f.write('}\n')
#         print(f"Đã ghi thành công {len(strings)} chuỗi vào file {file_path}")
#     except Exception as e:
#         print("Đã xảy ra lỗi khi ghi file:", e)

# if __name__ == "__main__":
#     strings_to_write = ["Hello", "World", "Welcome", "to", "OpenAI"]

#     c_file_path = "output.c"  # Đường dẫn tới file .c

#     # Ghi chuỗi vào file .c
#     write_to_c_file(strings_to_write, c_file_path)


# def find_substring_in_file(file_path, sub_string):
#     with open(file_path, 'r') as file:
#         previous_line = ""  # Dòng trước đó
#         line_number = 0
#         for line in file:
#             line_number += 1
#             if sub_string in line:
#                 print(f"Line {line_number - 1}: {previous_line.strip()}")  # In ra dòng phía trước
#                 print(f"Line {line_number}: {line.strip()}")  # In ra dòng chứa chuỗi con
#                 print(f"Position: {line.find(sub_string)}")  # In ra vị trí của chuỗi con trong dòng

#             previous_line = line  # Lưu trữ dòng hiện tại cho lần lặp tiếp theo

# def main():
#     file_path = "ten_tep.txt"  # Thay đổi thành đường dẫn tới tệp của bạn
#     sub_string = "slider_set_callback"  # Thay đổi thành chuỗi con bạn muốn tìm

#     find_substring_in_file(file_path, sub_string)

# if __name__ == "__main__":
#     main()

# list_keyword_to_break = ["*/",";","}"]
# def find_substring_in_file(file_path, sub_string):
#     index = -1
#     with open(file_path, 'r') as file:
#         lines_previous = ''
#         lines = file.readlines()  # Đọc tất cả các dòng trong file vào danh sách
#         line_number = len(lines)  # Số dòng trong file

#         for line in reversed(lines):  # Lặp ngược lại từ cuối danh sách đến đầu
#             line_number -= 1  # Giảm số dòng hiện tại
#             if sub_string in line:
#                 print(f"Line {line_number + 1}: {line}")  # In ra dòng chứa chuỗi con và số dòng tương ứng
#                 # Tìm chỉ số của 'Function_name'
#                 for keyword_index in list_keyword_to_break:
#                     index = line.find(keyword_index) 
#                     if(index != -1):
#                       break
        
                    

# def main():
#     file_path = "ten_tep.txt"  # Thay đổi thành đường dẫn tới tệp của bạn
#     sub_string = "slider_set_callback"  # Thay đổi thành chuỗi con bạn muốn tìm

#     find_substring_in_file(file_path, sub_string)

# if __name__ == "__main__":
#     main()


# list_keyword_to_break = [   "*/"  ,  ";"   ,  "}"  ]
# def find_substring_in_file(file_path, sub_string):
#     is_index_name_function_found = False
#     index_keyword_found = -1
#     with open(file_path, 'r') as file:
#         line_number = 0
#         for line in file:
#             line_number += 1
#             if(is_index_name_function_found == True):
#                 for keyword_index in list_keyword_to_break:
#                     index_keyword_found = line.find(keyword_index)
#             if sub_string in line:
#                 # print(f"Line {line_number}: {line.strip()}")  # In ra dòng chứa chuỗi con
#                 # print(f"Position: {line.find(sub_string)}")  # In ra vị trí của chuỗi con trong dòng
#                 is_index_name_function_found = True
#             else:
#                 is_index_name_function_found = False

# def main():
#     file_path = "ten_tep.txt"  # Thay đổi thành đường dẫn tới tệp của bạn
#     sub_string = "slider_set_callback"  # Thay đổi thành chuỗi con bạn muốn tìm

#     find_substring_in_file(file_path, sub_string)

# if __name__ == "__main__":
#     main()





# def find_substring(file_path, sub_string):
#     index_keyword = [True,True,True,True]
#     index_keyword_1 = [True,True,True,True]
#     with open(file_path, 'r') as file:
#         lines = file.readlines()  # Đọc tất cả các dòng trong file vào danh sách
#         line_number = len(lines)  # Số dòng trong file

#         # Lặp ngược lại từ cuối danh sách đến đầu
#         for line in reversed(lines):  
#             line_number -= 1  # Giảm số dòng hiện tại
#             if sub_string in line:
#                 print(f"Line {line_number + 1}: {line}")  # In ra dòng chứa chuỗi con và số dòng tương ứng
#                 # Tìm chỉ số của 'Function_name'
#                 index_keyword[0] = line.find('//') 
#                 index_keyword[1] = line.find('*/') 
#                 index_keyword[2] = line.find('/*') 
#                 index_keyword[3] = line.find(sub_string)
#                 index_keyword[4] = line.find(';')
#                 index_keyword[5] = line.find('{')
#                 index_keyword[6] = line.find('}')
#                 if( index_keyword[0] != -1 and index_keyword[1] != -1 ):
#                     if( index_keyword[0] <  index_keyword[1] ):
#                         print("Đúng")
#                     else:
#                         print("Sai")

#                 if( index_keyword[2] != -1 and index_keyword[3] != -1 ):
#                     if( index_keyword[2] >  index_keyword[3] ):
#                         print("Đúng")  
#                     else:
#                         print("Sai")   

#                 if( index_keyword[0] != -1 and index_keyword[3] != -1 ):            
#                     if( index_keyword[0] >  index_keyword[3] ):
#                         print("Đúng")  
#                     else:
#                         print("Sai")

#                 # if( index_keyword[4] != -1 and index_keyword[0] != -1 and index_keyword[1] != -1 ):         
#                 #     if( index_keyword[4] > index_keyword[0] and index_keyword[4] < index_keyword[1]):
#                 #         print("Đúng") 
#                 #     else:
#                 #         print("Sai")

                                          
                            
# def main():
#     file_path = "ten_tep.txt"  # Thay đổi thành đường dẫn tới tệp của bạn
#     sub_string = "slider_set_callback"  # Thay đổi thành chuỗi con bạn muốn tìm

#     find_substring(file_path, sub_string)

# if __name__ == "__main__":
#     main()


# def find_substring_in_file(file_path, sub_string):
#     with open(file_path, 'r') as file:
#         line_number = 0
#         for line in file:
#             line_number += 1
#             if sub_string in line:
#                 print(f"\nLine {line_number}: {line.strip()}")  # In ra dòng chứa chuỗi con
#                 print(f"Position: {line.find(sub_string)}")  # In ra vị trí của chuỗi con trong dòng

# def main():
#     file_path = "ten_tep.txt"  # Thay đổi thành đường dẫn tới tệp của bạn
#     sub_string = "slider_set_callback"  # Thay đổi thành chuỗi con bạn muốn tìm

#     find_substring_in_file(file_path, sub_string)

# if __name__ == "__main__":
#     main()



file_path = "ten_tep.txt"  # Thay đổi thành đường dẫn của tệp cần đọc
sub_string = "slider_set_callback"  # Chuỗi con cần tìm

with open(file_path, 'r') as file:
    lines = file.readlines()  # Đọc tất cả các dòng trong file vào một danh sách
for i, line in enumerate(lines):
    position_keyword_end_comment = []
    position_keyword_start_comment = []
    position_keyword_semicolon    = []
    position_sub_string           = []
    position_keyword_double_slash = []
    if sub_string in line:

        count = lines[i].count(f"{sub_string}")  # Số lần xuất hiện của chuỗi "*/"
        position_sub_string = [pos for pos, char in enumerate(line) if line.startswith(f"{sub_string}", pos)]  # Danh sách các vị trí của "*/" trên dòng hiện tại
        print(f"Found '{sub_string}' at line {i+1}, {count} times, position_sub_string: {position_sub_string}")

        if "*/" in lines[i]:
            count = lines[i].count("*/")  # Số lần xuất hiện của chuỗi "*/"
            position_keyword_end_comment = [pos for pos, char in enumerate(line) if line.startswith("*/", pos)]  # Danh sách các vị trí của "*/" trên dòng hiện tại
            print(f"Found '*/' before '{sub_string}' at line {i+1}, {count} times, position_keyword_end_comment: {position_keyword_end_comment}")
        else:
            print(f"No '*/' before '{sub_string}' at line {i+1}")

        if "/*" in lines[i]:
            count = lines[i].count("/*")  # Số lần xuất hiện của chuỗi "/*"
            position_keyword_start_comment = [pos for pos, char in enumerate(line) if line.startswith("/*", pos)]  # Danh sách các vị trí của "/*" trên dòng hiện tại
            print(f"Found '/*' before '{sub_string}' at line {i+1}, {count} times, position_keyword_start_comment: {position_keyword_start_comment}")
        else:
            print(f"No '/*' before '{sub_string}' at line {i+1}")
        
        if ";" in lines[i]:
            count = lines[i].count(";")  # Số lần xuất hiện của chuỗi ";"
            position_keyword_semicolon = [pos for pos, char in enumerate(line) if line.startswith(";", pos)]  # Danh sách các vị trí của ";" trên dòng hiện tại
            print(f"Found ';' before '{sub_string}' at line {i+1}, {count} times, position_keyword_semicolon: {position_keyword_semicolon}")
        else:
            print(f"No ';' before '{sub_string}' at line {i+1}")

        if "//" in lines[i]:
            count = lines[i].count("//")  # Số lần xuất hiện của chuỗi "//"
            position_keyword_double_slash = [pos for pos, char in enumerate(line) if line.startswith("//", pos)]  # Danh sách các vị trí của "//" trên dòng hiện tại
            print(f"Found '//' before '{sub_string}' at line {i+1}, {count} times, position_keyword_double_slash: {position_keyword_double_slash}")
        else:
            print(f"No '//' before '{sub_string}' at line {i+1}")


# is_sub_string_valid = False
# for index_sub_string in range(len(position_sub_string)):
#     for index_start_comment in range(len(position_keyword_start_comment)):
        
#         for index_keyword_double_slash in range(len(position_keyword_double_slash)):
#             if( (position_keyword_double_slash[index_keyword_double_slash] > position_keyword_start_comment[index_start_comment]) and (position_keyword_double_slash[index_keyword_double_slash] < position_sub_string[index_sub_string]) ):

#                 if(position_keyword_start_comment[index_start_comment] < position_sub_string[index_sub_string]):
#                     for index_end_comment in range(len(position_keyword_end_comment)):
#                         if( (position_keyword_end_comment[index_end_comment] < position_sub_string[index_sub_string]) and (position_keyword_end_comment[index_end_comment] > position_keyword_start_comment[index_start_comment]) ):
#                             is_sub_string_valid = True
#                             break
#                         else:
#                             is_sub_string_valid = False

# list_keyword_end_comment=[]
# for index_sub_string in range(len(position_sub_string)):
#     for index_end_comment in range(len(position_keyword_end_comment)):
#         if(position_keyword_end_comment[index_end_comment] < position_sub_string[index_sub_string]):
#             list_keyword_end_comment.append[]
        







    
        
        