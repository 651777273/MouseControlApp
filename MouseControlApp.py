import tkinter as tk
from pynput.mouse import Controller as MouseController
import keyboard
import threading
import time

# 初始化鼠标控制器
mouse = MouseController()
# 主要用到两个库：
# pynput （控制鼠标和键盘） ，keyboard （监听键盘按键）  pip install pynput keyboard
#程序有一个窗口界面 ，我们可以用 tkinter（Python内置的GUI库）来做，非常适合做这种轻量级界面！

# 目标位置定义
positions = {
    '1': (500, 300),  # A点
    '2': (700, 400),  # B点
    '3': (900, 500)  # C点
}


class MouseControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("鼠标控制程序")
        self.root.geometry("400x200")

        # 标签：显示当前位置
        self.position_label = tk.Label(root, text="当前鼠标位置: ", font=("Arial", 12))
        self.position_label.pack(pady=10)

        # 标签：显示移动动作
        self.action_label = tk.Label(root, text="操作提示: ", font=("Arial", 12))
        self.action_label.pack(pady=10)

        # 启动后台线程监听键盘
        self.running = True
        threading.Thread(target=self.listen_keyboard, daemon=True).start()

        # 定时刷新鼠标位置
        self.update_mouse_position()

    def update_mouse_position(self):
        pos = mouse.position
        self.position_label.config(text=f"当前鼠标位置: {pos}")
        self.root.after(100, self.update_mouse_position)  # 每100ms更新一次

    def listen_keyboard(self):
        while self.running:
            if keyboard.is_pressed('esc'):
                self.running = False
                self.root.quit()
                break

            if keyboard.is_pressed('p'):
                pos = mouse.position
                self.action_label.config(text=f"当前鼠标位置是: {pos}")
                time.sleep(0.3)

            for key in positions:
                if keyboard.is_pressed(key):
                    target_pos = positions[key]
                    mouse.position = target_pos
                    self.action_label.config(text=f"已移动到 {key} 号位置: {target_pos}")
                    time.sleep(0.3)


def main():
    root = tk.Tk()
    app = MouseControllerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
