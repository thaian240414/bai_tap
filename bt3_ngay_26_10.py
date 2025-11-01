# PROBLEM 3: THAY ĐỔI HÌNH ẢNH
# Problem Description
# Tạo ứng dụng GUI bằng guizero hiển thị một hình ảnh và 3 nút: “Mèo”, “Chó”, “Chim”. Khi nhấn nút, ảnh thay đổi tương ứng (cat.png, dog.png, bird.png).

# GUI Layout Requirements
# Sử dụng App(title="Image Viewer").
# Ảnh hiển thị ở giữa trên (dùng Picture).
# Dưới ảnh là 3 nút đặt theo hàng ngang (dùng Box chứa PushButton).
# Kích thước cửa sổ: 400x350.
# Ảnh nên vừa với cửa sổ (width khoảng 200–250px).
# Sơ đồ bố cục:

# ---------------------------------
# |             [ẢNH]              |
# |  [Mèo]   [Chó]   [Chim]       |
# ---------------------------------

from guizero import App, Picture, PushButton, Box

def cat():
    global pic
    pic.image = "cat.png"

def dog():
    global pic
    pic.image = "dog.png"

def bird():
    global pic
    pic.image = "bird.png"

app = App(title="Image Viewer", width=400, height=350)


pic = Picture(app, image="anm.png", width=200, height=200)


box = Box(app, align="top", layout="grid")

PushButton(box, text="Mèo", command=cat, grid=[0,0])
PushButton(box, text="Chó", command=dog, grid=[1,0])
PushButton(box, text="Chim", command=bird, grid=[2,0])

app.display()
