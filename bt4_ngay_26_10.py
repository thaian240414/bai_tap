# PROBLEM 4: TRÒ CHƠI OẲN TÙ TÌ
# Problem Description
# Tạo ứng dụng GUI bằng guizero có 3 nút “Kéo”, “Búa”, “Bao”. Khi bấm nút, chương trình chọn ngẫu nhiên nước đi cho máy và in ra console: You: Kéo | Computer: Bao | Result: Win

# GUI Layout Requirements
# Sử dụng App(title="Rock Paper Scissors").
# Phần tiêu đề Text("Chọn một trong ba:") hiển thị ở trên.
# 3 nút “Kéo”, “Búa”, “Bao” sắp theo hàng ngang, cách nhau đều.
# Có thể dùng Box để gom các nút.
# Kích thước cửa sổ: khoảng 300x200.
# Sơ đồ bố cục:

# ---------------------------------
# |       Chọn một trong ba:      |
# |  [Kéo]   [Búa]   [Bao]        |
# ---------------------------------

from guizero import App, PushButton, Text, Box
from random import choice



def keo():
    choi("Kéo")

def bua():
    choi("Búa")

def bao():
    choi("Bao")

def choi(luot_nguoi):
    luot_may = choice(["Kéo", "Búa", "Bao"])
    
    if luot_nguoi == luot_may:
        kq = "Tie"
    elif luot_nguoi == "Kéo" and luot_may == "Bao":
        kq = "win"
    elif luot_nguoi == "Búa" and luot_may == "Kéo":
        kq = "win"
    elif luot_nguoi == "Bao" and luot_may == "Búa":
        kq = "win"
    elif luot_nguoi == "Kéo" and luot_may == "Búa":
        kq = "lose"
    elif luot_nguoi == "Búa" and luot_may == "Bao":
        kq = "lose"
    elif luot_nguoi == "Bao" and luot_may == "Kéo":
        kq = "lose"
    else:
        kq = "Error?" 
    print(f"You:{luot_nguoi} | Computer: {luot_may}| Result: {kq}")

app = App(title="Rock Paper Scissors", width=300, height=200)

text = Text(app, text="Chọn một trong ba:")

box = Box(app, layout="grid")

PushButton(box, text="Kéo", command=keo, grid=[0,0])
PushButton(box, text="Búa", command=bua, grid=[2,0])
PushButton(box, text="Bao", command=bao, grid=[4,0])

app.display()
