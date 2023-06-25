# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

import re

text="hello,world"
pattern=r"world"
p1=re.compile(pattern)         #编译pattern
match=re.search(pattern,text)  #pattern没有编译进行search()
match1=re.search(p1,text)      #pattern编译后进行search()
if match :
    print("找到了匹配的",match.group(0))
else :
    print("没有找到匹配的")
if match1:
    print("找到了匹配的",match1.group(0))
else :
    print("没有找到匹配的")

text1="abababab"
pattern1=r"ab+"
match2=re.search(pattern1,text1)
print(match2.group(0))



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
