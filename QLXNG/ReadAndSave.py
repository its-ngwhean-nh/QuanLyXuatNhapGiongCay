path='D:/QuanLykhoPy/Nhom4_QLXNG/QLXNG/qlxng.txt'
#Biến path được sử dụng để lưu đường dẫn tới tệp tin qlxng.txt. Đường dẫn này được sử dụng trong hàm read() để mở tệp tin và đọc dữ liệu từ đó.

def save(line):
    """
    Lưu dòng dữ liệu vào tệp tin.

    Args:
        line (str): Dòng dữ liệu cần lưu.
    """
    with open('qlxng.txt', 'a', encoding='utf-8') as file:
        # Ghi dòng dữ liệu vào tệp tin, theo sau là ký tự xuống dòng
        file.write(str(line) + '\n')

def read():
    """
    Đọc dữ liệu từ tệp tin và trả về một danh sách các danh sách chứa dữ liệu.

    Returns:
        list: Một danh sách các danh sách chứa dữ liệu đọc từ tệp tin.
    """
    try:
        gc=[]
        # Mở tệp tin ở chế độ đọc ('r') với mã hóa 'utf-8'
        with open(path,'r', encoding='utf-8') as f:
            # Sử dụng vòng lặp for để thêm các dòng dữ liệu
            for i in f:
                data=i.strip() # strip loại bỏ các khoảng trắng thừa
                arr=data.split('')
                gc.append(arr)
        return gc
    except:
        pass