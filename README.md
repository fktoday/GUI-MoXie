# GUI-MoXie

默写卷生成器，自动为古诗文生成带画线句的默写卷。输出横线长度会根据字数长短自动调整。

![](https://cdn.jsdelivr.net/gh/fktoday/images@main/HEXO/iShot_2023-04-10_08.00.19.gif)

## 安装

`pip install PyQt5`

`pip install PyQt5-tools`

`pip install PyQt5designer`

## 打包

`pip install pyinstaller`

`pyinstaller -F -w main.py`

## 使用

1. 将古诗文复制进文本框中。
2. 输入古诗文本身所含所有标点符号，例如“，。：”。
3. 点击“奇数句留空”或“偶数句留空”，生成的结果即可复制。
