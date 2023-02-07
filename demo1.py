# utf - 8
print(520)
print(99.9)
print("hello world")
print('hell-world')
print(4 + 1)
#  输出数据到文件里
oo = open('E:/text.txt', 'a+')  # 文件不存在就创建 存在就继续追加
print('helloworld', file=oo)  # 输出使用 file=
oo.close()
