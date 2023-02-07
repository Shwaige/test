# float：浮点数 整数加小数
a = 3.14159
n1 = 1.1
n2 = 2.2
print(n1 + n2)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
print(Decimal(1.1)+Decimal(2.2))

# bool:布尔值
f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))
print(f1 + 1)
print(f2 + 1)

# str:字符串
str1 = '人生苦短，我用python'
str2 = "人生苦短，我用python"
str3 = """人生苦短，
我用python"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))