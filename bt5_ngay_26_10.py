# PROBLEM 5: ĐIỀU KHIỂN LED ẢO
# Problem Description
# Tạo ứng dụng GUI mô phỏng 3 đèn LED: “LED 1”, “LED 2”, “LED 3”. Mỗi LED có một nút riêng để bật/tắt. Khi nhấn nút, LED tương ứng đổi màu (từ xám sang xanh và ngược lại).

# GUI Layout Requirements
# Sử dụng App(title="LED Control").
# 3 LED hiển thị bằng Box hoặc Text, đặt hàng ngang ở giữa.
# Bên dưới là 3 nút điều khiển “LED 1”, “LED 2”, “LED 3”.
# Mỗi nút tương ứng với một LED.
# Cửa sổ kích thước khoảng 400x300.
# Khi LED bật → đổi màu nền Box/Text sang “green”.
# Khi tắt → đổi lại “gray”.
# Sơ đồ bố cục:

# ---------------------------------------
# |   [LED1]   [LED2]   [LED3]          |
# |   [Nút 1]  [Nút 2]  [Nút 3]         |
# ---------------------------------------

from guizero import App, Box, PushButton, Text

def dieu_khien_led1():
    if led1.bg == "gray":
        led1.bg = "green"
    elif led1.bg == "green":
        led1.bg = "gray"


def dieu_khien_led2():
    if led2.bg == "gray":
        led2.bg = "green"
    elif led2.bg == "green":
        led2.bg = "gray"


def dieu_khien_led3():
    if led3.bg == "gray":
        led3.bg = "green"
    elif led3.bg == "green":
        led3.bg = "gray"


app = App(title="LED Control", width=400, height=300)


box_led = Box(app, layout="grid", align="top")

led1 = Text(box_led, text="LED 1", grid=[0,0], bg="gray", size=14)

led2 = Text(box_led, text="LED 2", grid=[1,0], bg="gray", size=14)

led3 = Text(box_led, text="LED 3", grid=[2,0], bg="gray", size=14)

box_nut = Box(app, layout="grid", align="top")

PushButton(box_nut, text="Nút 1", grid=[0,0], command=dieu_khien_led1)

PushButton(box_nut, text="Nút 2", grid=[1,0], command=dieu_khien_led2)

PushButton(box_nut, text="Nút 3", grid=[2,0], command=dieu_khien_led3)

app.display()