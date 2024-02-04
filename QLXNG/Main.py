from tkinter import *
from ReadAndSave import *

from tkinter import messagebox
from tkinter import simpledialog




def Add(): ##them thong tin cay
    #dung format de canh le dung get() de lay gia tri nhap vao 
    line = "{:<40}{:<40}{:<40}{:<40}{:<40}".format(treeCode.get(), name.get(), alike.get(), day.get(), money.get())
    #nếu các ô nhập vào rỗng thì hiển thị thông báo lỗi
    if treeCode.get() == "" or name.get() == "" or alike.get() == "" or day.get() == "" or money.get() == "":
        #dùng messagebox để hiển thị thông báo lỗi, showinfo để hiển thị thông báo
        messagebox.showinfo("Lỗi", "Bạn cần nhập đầy đủ thông tin.")
        return
   #mo file qlxng.txt de ghi thong tin cay vao
    SaveData(line)
    #hien thi thong tin cay vua nhap vao listbox
    Show()

#luu thong tin da nhap vao file qlxng.txt
def SaveData(data):
    #dung with open de mo file qlxng.txt de ghi thong tin cay vao dùng mode a để ghi thêm vào cuối file
    with open('qlxng.txt', 'a') as f:
        #ghi thong tin cay vao file \n de xuong dong
        #f.write để ghi thong tin cay vao file ,data là thong tin cay
        f.write(data + '\n')


def Show():
    gc=read()
    listbox.delet(0,END)
    for i in gc:
        #dua thong tin cay vao listbox
        listbox.insert(END,i) #dua list giong cay vao listbox

        

def Show(): #hien thi danh sach da nhap
    # mo file qlxng.txt de doc thong tin cay dung utf-8 de doc tieng viet
    with open('qlxng.txt', 'r',encoding='utf-8') as file:
        # dùng readline() doc tung dong
        data = file.readlines()

    # dùng lĩstbox.delete() để xóa listbox chạy từ 0 đến hết
    listbox.delete(0, END)

    # duyet qua tung dong trong file item tẻong
    for item in data:
       #dùng listbox.insert() để hiển thị thông tin cay vào listbox END để hiển thị từ cuối lên, item.strip() để loại bỏ các khoảng trắng thừa
        listbox.insert(END, item.strip())
        



        
    







def DeleteByTreeCode():
    """
    Xoá cây theo mã cây.
    Hàm này yêu cầu người dùng nhập mã cây muốn xoá. Sau đó, hàm sẽ xoá các mục trong listbox có mã cây bắt đầu bằng mã cây đã nhập.
    Hàm cũng sẽ mở file 'qlxng.txt' để đọc thông tin cây. Sau đó, nếu dòng nào không bắt đầu bằng mã cây đã nhập, hàm sẽ ghi lại dòng đó vào file.
    """
    # Ask the user for the tree code
    treeCode = simpledialog.askstring("", "Nhập mã cây muốn xoá")

    # Delete the item from the listbox
    i = 0
#dùng while để duyệt qua từng dòng trong listbox .size() là số dòng trong listbox
    while i < listbox.size():
        #nếu listbox.get(i) bắt đầu bằng mã cây đã nhập thì xóa dòng đó dùng .startwith() để kiểm tra xem dòng đó có bắt đầu bằng mã cây đã nhập hay không
        if listbox.get(i).startswith(treeCode):
            #listbox.delete(i) để xóa dòng đó
            listbox.delete(i)
        else:
            #nếu không thì tăng i lên 1 i là số dòng trong listbox
            i += 1
    #mo file qlxng.txt de doc thong tin cay
    with open('qlxng.txt', 'r') as file:
        # doc tung dong trong file
        lines = file.readlines()
        #mở file qlxng.txt de ghi thong tin cay vao duyệt qua vòng for từng dòng trong file sau đó nếu dòng đó không bắt đầu bằng mã cây đã nhập thì ghi lại dòng đó vào file
    with open('qlxng.txt', 'w') as file:
        for line in lines:
            if not line.startswith(treeCode):
                file.write(line)
                




def DeleteList():  #xoá danh sách
    #dung messagebox de hien thi thong bao va askyesno de hien thi yes no
    messagebox.askyesno("Xoá danh sách", "Bạn muốn xoá danh sách hiện tại chứ?")
    
    # mo file qlxng.txt de ghi thong tin cay vao
    with open('qlxng.txt', 'w') as file:
    
        file.write("")
    # xoa listbox
        listbox.delete(0, END)
  
   


#root là cửa sổ chính =Tk()là tên cửa sổ
root=Tk()
#khai báo các biến theo kiểu stringVar
treeCode =StringVar() #mã cây
name =StringVar() #tên cây
alike=StringVar()#giống cây
day=StringVar()#ngày nhập
money=StringVar()#giá tiền



#cửa sổ root title là tiêu đề cửa sổ
root.title('Quản Lý Nhập Xuất Cây')
#độ rộng khung cửa sổ 
#minsize là độ rộng tối thiểu của cửa sổ
root.minsize(height=500,width=500)
#tiêu đề forn chữ trong cửa sổ
#fame là khung chứa các chức năng =Frame(root) là tên khung
frame = Frame(root)
#frame.grid(row=0) là vị trí của khung row là hàng 0 là hàng đầu tiên
frame.grid(row=0)
#label là tiêu đề trong khung chứa các chức năng dùng màu đen font là kiểu chữ cambria width là độ rộng, anchor là căn chỉnh chữ center là giữa .grid là vị trí của tiêu đề
Label(frame, text="                      Chương trình quản lý", fg='black', font=('cambria',16), width=25, anchor='center').grid(row=2, column=0)







#tạo xửa sổ làm việc
#listbox là khung hiển thị danh sách các cây=Listbox(root,width=113,height=20) là tên khung
listbox=Listbox(root,width=113,height=20)
#listbox.grid(row=1,columnspan=2) là vị trí của khung row là hàng 1 là hàng thứ 2 columnspan là độ rộng của khung
listbox.grid(row=1,columnspan=2)

#tạo các ô nhập thông tin Lable là tiêu đề Entry là ô nhập thông tin. root là cửa sổ chính,text là tiêu đề của ô nhập thông tin width là độ rộng của ô nhập thông tin textvariable là tên biến entry là tên ô nhập thông tin
Label(root,text='Mã cây:'.center(30)).grid(row = 2, column=0 ) # mã cây
Entry(root,width=30,textvariable=treeCode).grid(row = 2,column=1)

Label(root,text='Tên cây:'.center(30)).grid(row = 3, column=0 ) #tên cây
Entry(root,width=30,textvariable=name).grid(row = 3,column=1)

Label(root,text='Giống cây:'.center(30)).grid(row = 4, column=0 ) #giống
Entry(root,width=30,textvariable=alike).grid(row = 4,column=1)

Label(root,text='Ngày nhập:'.center(30)).grid(row = 5, column=0 ) #ngày nhập
Entry(root,width=30,textvariable=day).grid(row = 5,column=1)

Label(root,text='Giá tiền:'.center(30)).grid(row = 6, column=0 ) #giá
Entry(root,width=30,textvariable=money).grid(row = 6,column=1)



button=Frame(root)

#tạo các ô chức năng
#Button là tên nút chức năng text là tiêu đề của nút chức năng command là tên hàm khi nhấn vào nút chức năng thì sẽ chạy hàm đó button là tên khung chứa các nút chức năng command = là gán hàm cho nút chức năng .pack là vị trí của nút chức năng side là bên trái
Button(button,text ='Thêm',command = Add).pack(side=LEFT)
Button(button,text ='Xem danh sách',command= Show ).pack(side=LEFT)
Button(button,text ='Sắp xếp').pack(side=LEFT)      #chưa làm
Button(button,text ='Tìm vị trí ').pack(side=LEFT)         #chưa làm
Button(button,text ='Xoá theo mã cây ',command=DeleteByTreeCode).pack(side=LEFT)
Button(button,text ='Xoá danh sách ',command=DeleteList).pack(side=LEFT)
Button(button,text ='Thoát',command=root.quit).pack(side=LEFT)
#button.grid(row=7,column= 0) là vị trí của khung chứa các nút chức năng row là hàng 7 là hàng thứ 8 column là cột 0 là cột đầu tiên
button.grid(row=8,column= 0)


#root.mainloop() là vòng lặp chính của cửa sổ gọi ra cửa sổ chính
root.mainloop()

