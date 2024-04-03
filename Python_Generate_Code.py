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
