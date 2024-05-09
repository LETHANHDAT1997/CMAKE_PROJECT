# CÁC PHÉP TOÁN CƠ BẢN TRONG PYTHON
# Phép chia thông thường
a = 23/3
print(a) # 7.666666666666667

# Phép chia lấy phần nguyên
a= 23//3
print(a) # 7

# Phép mũ
a= 2 ** 3
print(a) # 8

# Phép toán ưu tiên
a= 1 + 10*10 +3
print(a) # 105

# CHUỖI TRONG PYTHON
# Chuỗi trong python có thể sử dụng '' hoặc ""
# VD: 'hello', "hello"
# Trong Python thì ta có thể sử dụng số âm để biểu thị vị trí,nó được gọi chỉ mục ngược
# Character     : h  e  l  l  o
# Index         : 0  1  2  3  4
# Reverse Index : 0 -4 -3 -2 -1
# Chỉ mục ngược hữu ích khi bạn muốn lấy giá trị từ cuối chuỗi về trước nhưng bạn không biết chính xác độ dài chuỗi,chỉ cần sử dụng -1
# Một tính năng hay nữa đó là slicing,nó cho phép bạn lấy một phần của chuỗi từ một vị trí bất kỳ và theo hướng tùy ý từ trái sang hoặc từ phải sang
# Syntax: [start:stop:step]
#          start: vị trí bắt đầu
#          stop: vị trí kết thúc (lưu ý không bao gồm vị trí stop)
#          step: là vị trí phần từ tiếp theo sẽ lấy (mốc từ vị trí phần tử đã lấy trước đó)
# VD: mystring = 'abcdefghijk'
#     mystring[2:]    //  Output: cdefghijk
#     mystring[:3]    //  Output: abc
#     mystring[3:6]   //  Output: def
#     mystring[::]    //  Output: abcdefghijk
#     mystring[::3]   //  Output: adgj
#     mystring[2:7:2] //  Output: ceg
#     mystring[::-1]  //  Output: kjihgfedcba  //lấy từ vị trí cuối cùng đi lên đầu

# Hàm enumerate() đếm chỉ mục một cách tự động
# VD: for item in enumerate('abcde'):
#         print(item)
#     kết quả: (0,'a')
#              (1,'b')
#              (2,'c')
#              (3,'d')
#              (4,'e')
# Hoặc có thể sử dụng như sau:
# for index,item in enumerate('abcde'):
#     print(index)
#     print(item)

# Hàm zip() như tên gọi dùng để liên kết các kiểu dữ liệu lại với nhau để tạo thành một tuple
# VD: mylist1 = [1,2,3]
#     mylist2 = ['a','b','c']
#     zip(mylist1,mylist2) // Kết quả sẽ in ra địa chỉ bộ nhớ mà chương trình zip sử dụng để chạy
# Để in ra từng phần tử đã zip ta làm như sau
# for item in zip(mylist1,mylist2):
#       print(item)
# Để nén các dữ liệu thành một list ta làm như sau
#  list(zip(mylist1,mylist2))
#  Lưu ý: zip() sẽ zip những giá trị có chung chỉ mục,nếu có các tập dữ liệu có độ dài không giống nhau thì hàm zip() sẽ bỏ qua các giá trị có chỉ mục bị thừa ra và sẽ không có cảnh báo lỗi

# def myfunc(*arg):
#       for item in args:
#           print(item)
# myfunc(40,60,100,1,34)
# Kết quả: 40
#          60
#          100
#          1
#          34

# def myfunc(**kwargs):
#       print(kwargs)
#       if 'fruit' in kwargs:
#           print('My fruit of choice is {}'.format(kwargs['fruit']))
#       else:
#           print('I did not find any fruit here')
# myfunc(fruit='apple',veggie='lettuce')
# Kết quả: {'fruit':'apple','veggie':'lettuce'}
#          My fruit of choice is apple

# def myfunc(*arg,**kwargs):
#       print(arg)
#       print(kwargs)
#       print('I would like {} {}.format(arg[0],kwargs['food']))
# myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')
# Kết quả: (10,20,30)
#          {'fruit':'orange','food':'egss','animal':'dog'}
#          I would like 10 eggs