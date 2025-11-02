
from guizero import App, Text, PushButton, Box

input_str = ""
app = App(title = "Máy tính bỏ túi", width = 530, height = 400, bg = "lightyellow")
def math(word):
    global input_str
    input_str += word
    result.value = input_str
def calculator():
    global input_str
    try:
        calculate_reuse = eval(input_str)
        result.value = calculate_reuse
    except ZeroDivisionError:
        result.value = "ERROR"
    except SyntaxError:
        result.value = "ERROR"
def delete():
    global input_str
    input_str = ""
    result.value = input_str
box_result = Box(app, width = 530, height = 100, border = True)
result = Text(box_result, text = "0", size = 25, color = "black", align = "right")
box_control = Box(app, width = 530, height = 300, border = True, layout = "grid")
for row in range(3):
    for column in range(3):
        btn = PushButton(box_control, grid = [column,row], width = 15, height = 3, text = "1", command = math, args = ["1"])
btn_2 = PushButton(box_control, grid = [1,2], width = 15, height = 3, text = "2", command = math, args = ["2"])
btn_3 = PushButton(box_control, grid = [0,2], width = 15, height = 3, text = "3", command = math, args = ["3"])
btn_4 = PushButton(box_control, grid = [2,1], width = 15, height = 3, text = "4", command = math, args = ["4"])
btn_5 = PushButton(box_control, grid = [1,1], width = 15, height = 3, text = "5", command = math, args = ["5"])
btn_6 = PushButton(box_control, grid = [0,1], width = 15, height = 3, text = "6", command = math, args = ["6"])
btn_7 = PushButton(box_control, grid = [2,0], width = 15, height = 3, text = "7", command = math, args = ["7"])
btn_8 = PushButton(box_control, grid = [1,0], width = 15, height = 3, text = "8", command = math, args = ["8"])
btn_9 = PushButton(box_control, grid = [0,0], width = 15, height = 3, text = "9", command = math, args = ["9"])
btn_plus = PushButton(box_control, grid = [3,0], width = 15, height = 3, text = "+", command = math, args = ["+"])
btn_minus = PushButton(box_control, grid = [3,1], width = 15, height = 3, text = "-", command = math, args = ["-"])
btn_mutiplay = PushButton(box_control, grid = [3,2], width = 15, height = 3, text = "*", command = math, args = ["*"])
btn_divide = PushButton(box_control, grid = [3,3], width = 15, height = 3, text = "/", command = math, args = ["/"])
btn_AC = PushButton(box_control, grid = [0,3], width = 15, height = 3, text = "AC", command = delete)
btn_0 = PushButton(box_control, grid = [1,3], width = 15, height = 3, text = "0", command = math, args = ["0"])
btn_equanl = PushButton(box_control, grid = [2,3], width = 15, height = 3, text = "=", command = calculator)

app.display()
