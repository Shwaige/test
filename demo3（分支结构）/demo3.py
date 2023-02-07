#  选择结构
#  1、单分支结构   （如果 --- 就 ---）

# money = 1000  # 余额
# s = int(input("请输入取款金额"))
# if money >= s:  # 判断余额是否充足
#     money = money - s
#     print("取款成功，余额为", money)

#  2、双分支结构   （如果 --- 就 ---，不满足 ---  就 ---）

# a = int(input("请输入一个整数"))
# if a % 2 == 0:
#     print("你输入的是偶数")
# else:
#     print("你输入的是奇数")

#  3、多分支结构      （如果 a 就 a1，如果 b  就 b1....）

# a = int(input("输入一个分数"))
# if a > 90 and  a <= 100:
#     print("成绩为优秀")
# elif a > 70 and a <= 90:
#     print("成绩为良好")
# elif a >= 60 and a <= 70:
#     print("成绩为及格")
# elif a < 60:
#     print("成绩为不及格")
# else:
#     print("成绩输入错误")
#

#  4、嵌套 if

"""会员  >= 100  9折>=200   8折
非会员 >= 100  9.5折>=200   8.5折"""
vip = input("您是会员嘛？y/n")
if vip == "y":
    a = int(input("输入你的购物金额："))
    if a >= 200:
        a = a * 0.8
        print("请支付：", a, "元")
    elif a >= 100 and a < 200:
        a = a * 0.9
        print("请支付：", a, "元")
    else:
        print("请支付：", a, "元")
elif vip == "n":
    a = int(input("输入你的购物金额："))
    if a >= 200:
        a = a * 0.85
        print("请支付：", a, "元")
    elif a >= 100 and a < 200:
        a = a * 0.95
        print("请支付：", a, "元")
    else:
        print("请支付：", a, "元")
else:
    print("你输入有误")
