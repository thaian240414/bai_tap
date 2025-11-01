from guizero import App, Text, Box, PushButton

def check(answer):
    if answer == "Hà Nội":
        print("Đúng!")
    else:
        print("Sai!")

app = App(title="Quiz App", width=300, height=200)

text = Text(app, text="Thủ đô của Việt Nam là gì?")

box = Box(app, layout="grid")

button1 = PushButton(box, command=check, text="Hà Nội", args=["Hà Nội"], grid=[0,0])

button2 = PushButton(box, command=check, text="TP.HCM", args=["TP.HCM"], grid=[1,0])

button3 = PushButton(box, command=check, text="Đà Nẵng", args=["Đà Nẵng"], grid=[2,0])

app.display()
