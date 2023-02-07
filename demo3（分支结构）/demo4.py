#  条件表达式
num_a = int(input("输入一个整数："))
num_b = int(input("输入另一个整数："))
"""
if num_a > num_b:
    print(num_a, ">", num_b)
elif num_a < num_b:
    print(num_a, "<", num_b)
else:
    print(num_a, "=", num_b)
"""
print(str(num_a) + ">=" + str(num_b) if num_a >= num_b else str(num_a) + "<" + str(num_b))
