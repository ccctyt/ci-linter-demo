# main.py - 不符合 PEP8 的代码示例

def  say_hello ( name ) :  # 多余空格，缺少空行
    print("Hello, " + name) # 行太长（虽然不严重），但可以加点内容让它变长
    if True:
     print("This is bad indentation")  # 缩进错误（使用了空格和制表符混合？这里用4空格但故意错位）

def long_function():
    x = "This is a very long line that exceeds the 79 character limit recommended by PEP8, so it should trigger a warning or error when flake8 runs"
    return x

say_hello("World")
