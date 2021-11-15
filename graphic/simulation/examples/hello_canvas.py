from tkinter import Tk, Canvas

tk = Tk()
tk.title("Hello Canvas")

canvas = Canvas(tk, width=600, height=600)
canvas.grid(row=0, column=0)
canvas.create_line(0, 0, 300, 300,
                    fill="red", width=3
)
canvas.create_oval(
    200,200,500,400,
    width = 3,
    outline = "#aa3355",
    fill = "#cc3355"
)

canvas.create_rectangle(
    40,400,500,500,
    width = 3,
    outline = "#aa3355"
)
canvas.create_polygon(
    [40, 200, 300, 450, 600, 0],
    width=3,
    outline="#aa3355",
    fill = ''
)

canvas.create_text(
    300, 520,
    text = "Weird drawing flex bruh",
    fill = "red",
    font = "Helvetica 20 bold"
)
tk.mainloop()