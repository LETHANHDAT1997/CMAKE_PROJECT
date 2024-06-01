# python -m pip install colorama
# Import thư viện logging để tinh chỉnh thông tin xuất ra trên terminal
import logging
# Import colorama để chỉnh màu cho chữ và nền trong terminal
#  - init dùng để khởi tạo thư viện gồm :
#   + autoreset : True nghĩa là cứ sau một dòng thì sẽ tự động quay lại màu mặc định, False thì phải dùng lệnh Style.RESET_ALL sau câu lệnh mình in ra để reset lại màu
#   + convert   : Đây là một tham số tùy chọn cho biết liệu colorama có tự động chuyển đổi các mã màu ANSI thành mã màu phù hợp với terminal hiện tại không. Nếu đặt là True, colorama sẽ tự động chuyển đổi. Mặc định là True.
#   + strip     : Đây là một tham số tùy chọn cho biết liệu colorama có loại bỏ các mã màu ANSI khỏi các chuỗi không. Nếu đặt là True, colorama sẽ loại bỏ các mã màu ANSI. Mặc định là False.
#   + wrap      : True sẽ giúp hàm print thông thường có thể đổi màu chữ
#  - Fore dùng để đổi màu chữ gồm một số màu có sẵn như :
#   + BLACK
#   + RED
#   + GREEN
#   + YELLOW
#   + BLUE
#   + MAGENTA
#   + CYAN
#   + WHITE
#  - Back dùng để đổi màu background tương tự như Fore
#  - Style dùng để chỉnh các thông số cho chữ chẳng hạn như in đậm, in nghiêng, hoặc in nền.
#       + NORMAL: Trả về kiểu văn bản bình thường.
#       + BRIGHT hoặc Style.DIM: Chuyển sang kiểu văn bản sáng hoặc tối.
#       + NORMAL: Trả về kiểu văn bản bình thường.
#       + BRIGHT hoặc Style.DIM: Chuyển sang kiểu văn bản sáng hoặc tối.
#       + RESET_ALL: Đặt lại tất cả các kiểu văn bản đã được thiết lập trở về mặc định.
from colorama import init, Fore, Back, Style

class Print_Fortmat():
    # -> None: Dấu mũi tên này chỉ ra kiểu trả về của hàm khởi tạo, trong trường hợp này là None.
    def __init__(self,string_infor = 'None') -> None:      
        # Khởi tạo colorama
        # autoreset = True nghĩa là cứ sau một dòng thì sẽ tự động quay lại màu mặc định, False thì phải dùng lệnh Style.RESET_ALL sau câu lệnh mình in ra để reset lại màu
        init(autoreset = False)

        # Tạo logger
        self.logger = logging.getLogger(string_infor)
        self.logger.setLevel(logging.DEBUG)

        # Tạo console handler và thiết lập cấp độ log
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)

        # Tạo file handler và thiết lập cấp độ log
        self.file_handler = logging.FileHandler('example.log')
        self.file_handler.setLevel(logging.ERROR)
    
        # Tạo formatter và thêm vào các handler
        self.formatter = logging.Formatter()
        self.console_handler.setFormatter(self.formatter)
        self.file_handler.setFormatter(self.formatter)

        # Thêm các handler vào logger
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler) 

    def Print_Log_DEBUG(self,str_output ):
            self.formatter = logging.Formatter(f'{Fore.BLUE}%(levelname)s - %(name)s - %(message)s - %(filename)s - Line:%(lineno)s - %(asctime)s')
            self.console_handler.setFormatter(self.formatter)
            self.logger.debug(str_output) 

    def Print_Log_INFO(self,str_output ):
            self.formatter = logging.Formatter(f'{Fore.GREEN}%(levelname)s - %(name)s - %(message)s - %(filename)s - Line:%(lineno)s - %(asctime)s')
            self.console_handler.setFormatter(self.formatter)
            self.logger.info(str_output)               

    def Print_Log_WARNING(self,str_output ):
            self.formatter = logging.Formatter(f'{Fore.YELLOW}%(levelname)s - %(name)s - %(message)s - %(filename)s - Line:%(lineno)s - %(asctime)s')
            self.console_handler.setFormatter(self.formatter)
            self.logger.warning(str_output) 

    def Print_Log_ERROR(self,str_output ):
            self.formatter = logging.Formatter(f'{Fore.RED}%(levelname)s - %(name)s - %(message)s - %(filename)s - Line:%(lineno)s - %(asctime)s')
            self.console_handler.setFormatter(self.formatter)
            self.logger.error(str_output) 

if __name__ == "__main__":
    Log = Print_Fortmat()
    # Ghi log
    Log.Print_Log_ERROR('This is an info message')
    Log.Print_Log_DEBUG('This is a warning message')
    Log.Print_Log_INFO('This is an error message')
    Log.Print_Log_WARNING('This is a critical message')
