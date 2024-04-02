def extract_function_name(file_path):
    # Mở tệp để đọc
    with open(file_path, 'r') as file:
        # Đọc nội dung của tệp
        content = file.read()

    # Tìm chỉ số của 'Function_name'
    index = content.find('stop_webserver')

    # Nếu không tìm thấy 'Function_name', trả về None
    if index == -1:
        return None

    # Khởi tạo một chuỗi rỗng để lưu kết quả
    result = ''

    # Lặp ngược từ chỉ số của 'Function_name'
    for i in range(index - 1, -1, -1):
        # Nếu ký tự là '/', ';' hoặc '<', dừng vòng lặp
        if content[i] in ['}', '>', '<']:
            break
        # Ngược lại, thêm ký tự vào kết quả
        result = content[i] + result

    # Trả về kết quả
    return result
# Giả sử tệp cần đọc là 'source_code.txt'
file_path = 'ten_tep.txt'
# Gọi hàm và in kết quả
print(f"Giá trị trích xuất là: {extract_function_name(file_path)}")


# Đọc tệp và trích xuất giá trị sau chuỗi "Function_name"
def extract_function_values(file_path):
    # Mở tệp để đọc
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Tìm chỉ số của "Function_name"
    index = content.find('stop_webserver')
    
    # Nếu không tìm thấy "Function_name", trả về danh sách rỗng
    if index == -1:
        return []
    
    # Tìm chỉ số của ký tự '/' hoặc ';', hoặc '<' tiếp theo sau "Function_name"
    end_index = min(
        [content.find(char, index) for char in ['?', ';', '<'] if content.find(char, index) != -1] + [len(content)]
    )
    
    # Trích xuất giá trị giữa "Function_name" và ký tự kết thúc
    values = content[index+len('stop_webserver'):end_index].strip()
    
    # Trả về các giá trị đã trích xuất
    return values

# Ví dụ sử dụng:
# Giả sử tệp 'example.txt' chứa nội dung chúng ta muốn xử lý
result = extract_function_values('ten_tep.txt')
print(result)

# Lưu ý: Tên tệp thực tế cần được thay thế bằng 'example.txt' trong ví dụ sử dụng ở trên.
# Vì không có tệp được cung cấp, tôi không thể thực hiện hàm với tệp thực tế.


