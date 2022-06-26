name = '张三'
age = 20

print(type(name),type(age))
print('我叫'+name+'今年'+str(age)+'岁')#将str类型与int类型连接时报错

print('----------------------------str()将其他类型转为str类型------')
a = 10
b = 198.8
c = False

print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('----------------------------int()将其他类型转为int类型------')

s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(int(s1),int(f1),int(ff))

print('----------------------------float()将其他类型转为float类型------')
s1 = '128.98'
s2 = '76'
ff = True
s3 = 'hello'
print(float(s1),float(s2),float(ff))
#单行注释
'''嘿嘿，
我是
多行
注释'''