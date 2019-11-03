"""
作者：李亮亮
功能：五角星绘制
版本号：2.0
日期：2019/7/3
新增功能：使用循环和递归绘制不同大小的五角星
"""
import turtle

def draw_pentagram(size):

    """
    绘制五角星
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

def main():
    """
    主函数

    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('blue')
    size=50
    while size <= 150:
        #调用函数
        draw_pentagram(size )
        size += 10

    turtle.exitonclick()


if __name__ == '__main__':
    main()
