from tkinter import *
from tkinter.ttk import *


class Win_l6ohmo1m:
    def __init__(self):
        self.root = self.__win()
        self.tk_table_l6ohn3by = self.__tk_table_l6ohn3by()
        self.tk_select_box_l6ohnodx = self.__tk_select_box_l6ohnodx()
        self.tk_progressbar_l6ohnufj = self.__tk_progressbar_l6ohnufj()
        self.tk_label_frame_l6oho691 = Frame_l6oho691(self.root)
        self.tk_button_l6ohofi6 = self.__tk_button_l6ohofi6()
        self.tk_tabs_l6ohojjz = Frame_l6ohojjz(self.root)
        self.tk_input_l6ohp262 = self.__tk_input_l6ohp262()
        self.tk_text_l6ohpfcj = self.__tk_text_l6ohpfcj()

    def __win(self):
        root = Tk()
        root.title("我是标题 ~ Tkinter布局助手")
        # 设置大小 居中展示
        width = 624
        height = 533
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False, height=False)
        return root

    def __tk_table_l6ohn3by(self):
        # 表头字段 表头宽度
        columns = {"ID": 50, "网站名": 100, "地址": 300}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self.root, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        data = [
            [1, "github", "https://github.com/iamxcd/tkinter-helper"],
            [2, "演示地址", "https://www.pytk.net/tkinter-helper"]
        ]

        # 导入初始数据
        for values in data:
            tk_table.insert('', END, values=values)

        tk_table.place(x=10, y=10, width=450, height=70)
        return tk_table

    def __tk_select_box_l6ohnodx(self):
        cb = Combobox(self.root, state="readonly")
        cb['values'] = ("下拉选择框", "Python", "Tkinter Helper")
        cb.place(x=470, y=10, width=150, height=24)
        return cb

    def __tk_progressbar_l6ohnufj(self):
        progressbar = Progressbar(self.root, orient=HORIZONTAL)
        progressbar.place(x=20, y=480, width=544, height=24)
        return progressbar

    def __tk_button_l6ohofi6(self):
        btn = Button(self.root, text="按钮")
        btn.place(x=220, y=300, width=50, height=24)
        return btn

    def __tk_input_l6ohp262(self):
        ipt = Entry(self.root)
        ipt.place(x=50, y=300, width=150, height=24)
        return ipt

    def __tk_text_l6ohpfcj(self):
        text = Text(self.root)
        text.place(x=50, y=350, width=518, height=115)
        return text


class Frame_l6oho691:
    def __init__(self, parent):
        self.root = self.__frame(parent)

    def __frame(self, parent):
        frame = LabelFrame(parent, text="标签容器")
        frame.place(x=380, y=100, width=200, height=150)
        return frame


class Frame_l6ohojjz:
    def __init__(self, parent):
        self.root = self.__frame(parent)

    def __frame(self, parent):
        frame = Notebook(parent)

        tk_tabs_l6ohojjz_0 = Frame_l6ohojjz_0(frame)
        frame.add(tk_tabs_l6ohojjz_0.root, text="选项卡1")

        tk_tabs_l6ohojjz_1 = Frame_l6ohojjz_1(frame)
        frame.add(tk_tabs_l6ohojjz_1.root, text="选项卡2")

        frame.place(x=30, y=90, width=319, height=176)
        return frame


class Frame_l6ohojjz_0:
    def __init__(self, parent):
        self.root = self.__frame(parent)

    def __frame(self, parent):
        frame = Frame(parent)
        frame.place(x=30, y=90, width=319, height=176)
        return frame


class Frame_l6ohojjz_1:
    def __init__(self, parent):
        self.root = self.__frame(parent)

    def __frame(self, parent):
        frame = Frame(parent)
        frame.place(x=30, y=90, width=319, height=176)
        return frame


def run():
    win = Win_l6ohmo1m()
    # TODO 绑定点击事件或其他逻辑处理
    win.root.mainloop()


if __name__ == "__main__":
    run()

