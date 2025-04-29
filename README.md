# MouseControlApp
一个基于 Python 的鼠标控制工具，通过键盘快捷键（1、2、3）将鼠标快速移动到指定坐标位置，并实时显示鼠标当前位置。

## ✨ 功能特点
- 实时显示鼠标当前指针坐标
- 键盘快捷键操作（1, 2, 3）
- 移动鼠标到预设位置
- 支持 Windows 平台
- 可打包为独立 `.exe` 文件，无需预装 Python
---

## 📦 环境要求
- Python 3.11
- `pynput`
- `keyboard`
- （GUI库 `tkinter` 是标准库，自带）
推荐使用 Conda 虚拟环境进行管理。

## 🚀 安装步骤
1. 克隆项目到本地：
git clone https://github.com/651777273/MouseControlApp
cd MouseControlApp
2.	创建并激活虚拟环境：
conda create -n mousecontrol python=3.11
conda activate mousecontrol
3.	安装依赖：
pip install -r requirements.txt
4.	运行程序：
python MouseControlApp.py

🛠️ 使用方法
•	打开程序后，会弹出一个窗口，显示实时鼠标坐标。
•	键盘操作：
o	按下 1：鼠标移动到位置 A
o	按下 2：鼠标移动到位置 B
o	按下 3：鼠标移动到位置 C
o	按下 Esc：退出程序
