# PROBLEM 2: QUAY SỐ NGẪU NHIÊN
# Problem Description
# Tạo ứng dụng GUI bằng guizero có một nút duy nhất “Quay số”. Khi bấm nút, in ra một số ngẫu nhiên từ 1 đến 100 trong console.

# GUI Layout Requirements
# Dùng App(title="Random Number").
# Một PushButton duy nhất đặt giữa màn hình.
# Có thể căn giữa bằng Box hoặc dùng align="top" và align="bottom" hợp lý.
# Kích thước cửa sổ: khoảng 200x150.
# Nút nên có kích thước vừa phải (width=10, height=2).
# Sơ đồ bố cục:

# ---------------------
# |                   |
# |     [Quay số]     |
# |                   |
# ---------------------


from guizero import App, PushButton, Box
from random import randint

def spin_number():
    number = randint(1, 100)
    print(f"Số ngẫu nhiên: {number}")


app = App(title="Random Number", width=200, height=150)


box = Box(app, align="top", height="fill", width="fill")


button = PushButton(box, text="Quay số", command=spin_number, width=10, height=2)

app.display()

